from typing import Optional
from sqlalchemy.orm import Session
from app.enums import EventType, PaymentStatus, SettlementStatus
from app.models import Merchant, PaymentEvent, Transaction
from sqlalchemy import asc, desc
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import joinedload
from sqlalchemy import func, and_, or_


# -------------------------------------------------------------------
# Merchant
# -------------------------------------------------------------------

def get_merchant_by_external_id(
    db: Session,
    merchant_id: str,
) -> Optional[Merchant]:
    return (
        db.query(Merchant)
        .filter(Merchant.merchant_id == merchant_id)
        .first()
    )


def create_merchant(
    db: Session,
    merchant_id: str,
    merchant_name: str,
) -> Merchant:
    merchant = Merchant(
        merchant_id=merchant_id,
        merchant_name=merchant_name,
    )

    db.add(merchant)
    db.flush()

    return merchant


# -------------------------------------------------------------------
# Transaction
# -------------------------------------------------------------------

def get_transaction_by_external_id(
    db: Session,
    transaction_id: str,
) -> Optional[Transaction]:
    return (
        db.query(Transaction)
        .filter(Transaction.transaction_id == transaction_id)
        .first()
    )


def create_transaction(
    db: Session,
    transaction_id: str,
    merchant_pk: int,
    amount,
    currency: str,
) -> Transaction:
    transaction = Transaction(
        transaction_id=transaction_id,
        merchant_id=merchant_pk,
        amount=amount,
        currency=currency,
        payment_status=PaymentStatus.INITIATED,
        settlement_status=SettlementStatus.PENDING,
    )

    db.add(transaction)
    db.flush()

    return transaction


# -------------------------------------------------------------------
# Events
# -------------------------------------------------------------------

def get_event_by_event_id(
    db: Session,
    event_id: str,
) -> Optional[PaymentEvent]:
    return (
        db.query(PaymentEvent)
        .filter(PaymentEvent.event_id == event_id)
        .first()
    )


def create_event(
    db: Session,
    *,
    event_id: str,
    transaction_pk: int,
    external_transaction_id: str,
    merchant_pk: int,
    external_merchant_id: str,
    event_type: EventType,
    timestamp,
    payload,
) -> PaymentEvent:

    event = PaymentEvent(
        event_id=event_id,
        transaction_pk=transaction_pk,
        external_transaction_id=external_transaction_id,
        merchant_id=merchant_pk,
        external_merchant_id=external_merchant_id,
        event_type=event_type,
        event_timestamp=timestamp,
        raw_payload=payload,
    )

    db.add(event)

    return event


# -------------------------------------------------------------------
# Transaction State Update
# -------------------------------------------------------------------

def update_transaction_status(
    transaction: Transaction,
    event_type: EventType,
) -> None:

    if event_type == EventType.PAYMENT_INITIATED:
        transaction.payment_status = PaymentStatus.INITIATED

    elif event_type == EventType.PAYMENT_PROCESSED:
        transaction.payment_status = PaymentStatus.PROCESSED

    elif event_type == EventType.PAYMENT_FAILED:
        transaction.payment_status = PaymentStatus.FAILED

    elif event_type == EventType.SETTLED:
        transaction.settlement_status = SettlementStatus.SETTLED

def list_transactions(
    db: Session,
    merchant_id: str | None = None,
    payment_status: str | None = None,
    start_date=None,
    end_date=None,
    page: int = 1,
    page_size: int = 20,
    sort_by: str = "created_at",
    sort_order: str = "desc",
):
    query = (
        db.query(Transaction)
        .options(joinedload(Transaction.merchant))
    )

    # -------------------------
    # Merchant Filter
    # -------------------------

    if merchant_id:

        query = query.join(Merchant).filter(
            Merchant.merchant_id == merchant_id
        )

    # -------------------------
    # Payment Status Filter
    # -------------------------

    if payment_status:

        query = query.filter(
            Transaction.payment_status == payment_status
        )

    # -------------------------
    # Date Filters
    # -------------------------

    if start_date:

        query = query.filter(
            Transaction.created_at >= start_date
        )

    if end_date:

        query = query.filter(
            Transaction.created_at <= end_date
        )

    # -------------------------
    # Sorting
    # -------------------------

    sort_column = getattr(
        Transaction,
        sort_by,
        Transaction.created_at,
    )

    if sort_order.lower() == "asc":

        query = query.order_by(
            asc(sort_column)
        )

    else:

        query = query.order_by(
            desc(sort_column)
        )

    total = query.count()

    transactions = (
        query.offset(
            (page - 1) * page_size
        )
        .limit(page_size)
        .all()
    )

    return total, transactions

def get_transaction_details(
    db: Session,
    transaction_id: str,
):
    return (
        db.query(Transaction)
        .options(
            joinedload(Transaction.merchant),
            joinedload(Transaction.events),
        )
        .filter(
            Transaction.transaction_id == transaction_id
        )
        .first()
    )

def get_reconciliation_summary(db: Session):

    results = (
        db.query(
            Merchant.merchant_id,
            Merchant.merchant_name,

            func.count(Transaction.id).label("total_transactions"),

            func.count(
                Transaction.id
            ).filter(
                Transaction.payment_status == PaymentStatus.PROCESSED
            ).label("processed"),

            func.count(
                Transaction.id
            ).filter(
                Transaction.payment_status == PaymentStatus.FAILED
            ).label("failed"),

            func.count(
                Transaction.id
            ).filter(
                Transaction.settlement_status == SettlementStatus.SETTLED
            ).label("settled"),

            func.count(
                Transaction.id
            ).filter(
                Transaction.settlement_status == SettlementStatus.PENDING
            ).label("pending_settlement"),
        )
        .join(Merchant)
        .group_by(
            Merchant.id,
            Merchant.merchant_id,
            Merchant.merchant_name,
        )
        .all()
    )

    return results

def get_reconciliation_discrepancies(db: Session):

    return (

        db.query(Transaction)

        .join(Merchant)

        .options(
            joinedload(Transaction.merchant)
        )

        .filter(

            or_(

                and_(

                    Transaction.payment_status == PaymentStatus.PROCESSED,

                    Transaction.settlement_status == SettlementStatus.PENDING,

                ),

                and_(

                    Transaction.payment_status == PaymentStatus.FAILED,

                    Transaction.settlement_status == SettlementStatus.SETTLED,

                )

            )

        )

        .all()

    )