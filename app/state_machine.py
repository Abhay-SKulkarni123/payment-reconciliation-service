from app.enums import EventType
from app.enums import PaymentStatus
from app.enums import SettlementStatus
from app.models import Transaction


class TransactionStateMachine:

    @staticmethod
    def apply_event(
        transaction: Transaction,
        event_type: EventType,
    ) -> bool:

        # -------------------------------
        # payment initiated
        # -------------------------------

        if event_type == EventType.PAYMENT_INITIATED:

            transaction.payment_status = PaymentStatus.INITIATED
            return True

        # -------------------------------
        # payment processed
        # -------------------------------

        if event_type == EventType.PAYMENT_PROCESSED:

            if transaction.payment_status != PaymentStatus.INITIATED:
                return False

            transaction.payment_status = PaymentStatus.PROCESSED
            return True

        # -------------------------------
        # payment failed
        # -------------------------------

        if event_type == EventType.PAYMENT_FAILED:

            if transaction.payment_status != PaymentStatus.INITIATED:
                return False

            transaction.payment_status = PaymentStatus.FAILED
            return True

        # -------------------------------
        # settled
        # -------------------------------

        if event_type == EventType.SETTLED:

            if transaction.payment_status != PaymentStatus.PROCESSED:
                return False

            transaction.settlement_status = SettlementStatus.SETTLED
            return True

        return False