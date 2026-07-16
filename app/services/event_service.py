from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app import crud
from app.enums import EventType
from app.schemas.event import EventCreateRequest, EventResponse
from app.state_machine import TransactionStateMachine


class EventService:

    @staticmethod
    def ingest_event(
        db: Session,
        event: EventCreateRequest,
    ) -> EventResponse:
        """
        Ingest a payment lifecycle event.

        Responsibilities:
        - Idempotency
        - Merchant creation
        - Transaction creation
        - Event history preservation
        - Transaction state update
        """

        try:

            # ---------------------------------------------------------
            # Step 1 : Idempotency
            # ---------------------------------------------------------

            existing_event = crud.get_event_by_event_id(
                db=db,
                event_id=event.event_id,
            )

            if existing_event:

                existing_transaction = crud.get_transaction_by_external_id(
                db=db,
                transaction_id=event.transaction_id,
            )

                return EventResponse(
                    success=True,
                    message="Duplicate event ignored.",
                    event_id=event.event_id,
                    transaction_id=event.transaction_id,
                    payment_status=existing_transaction.payment_status.value,
                    settlement_status=existing_transaction.settlement_status.value,
                )

            # ---------------------------------------------------------
            # Step 2 : Merchant
            # ---------------------------------------------------------

            merchant = crud.get_merchant_by_external_id(
                db=db,
                merchant_id=event.merchant_id,
            )

            if merchant is None:

                merchant = crud.create_merchant(
                    db=db,
                    merchant_id=event.merchant_id,
                    merchant_name=event.merchant_name,
                )

            # ---------------------------------------------------------
            # Step 3 : Transaction
            # ---------------------------------------------------------

            transaction = crud.get_transaction_by_external_id(
                db=db,
                transaction_id=event.transaction_id,
            )

            if transaction is None:

                transaction = crud.create_transaction(
                    db=db,
                    transaction_id=event.transaction_id,
                    merchant_pk=merchant.id,
                    amount=event.amount,
                    currency=event.currency,
                )

            # ---------------------------------------------------------
            # Step 4 : Save Event History
            # ---------------------------------------------------------

            crud.create_event(
                db=db,
                event_id=event.event_id,
                transaction_pk=transaction.id,
                external_transaction_id=event.transaction_id,
                merchant_pk=merchant.id,
                external_merchant_id=event.merchant_id,
                event_type=event.event_type,
                timestamp=event.timestamp,
                payload=event.model_dump(mode="json"),
            )

            # ---------------------------------------------------------
            # Step 5 : Update Transaction State
            # ---------------------------------------------------------

            transition_applied = TransactionStateMachine.apply_event(
                transaction=transaction,
                event_type=event.event_type,
            )

            # ---------------------------------------------------------
            # Step 6 : Commit
            # ---------------------------------------------------------

            db.commit()

            db.refresh(transaction)

            message = (
                "Event processed successfully."
                if transition_applied
                else "Event recorded. Invalid state transition detected."
            )

            return EventResponse(
                success=True,
                message=message,
                event_id=event.event_id,
                transaction_id=transaction.transaction_id,
                payment_status=transaction.payment_status.value,
                settlement_status=transaction.settlement_status.value,
            )

        except SQLAlchemyError:

            db.rollback()
            raise

        except Exception:

            db.rollback()
            raise