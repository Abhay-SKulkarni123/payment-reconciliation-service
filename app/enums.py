from enum import Enum


class EventType(str, Enum):
    PAYMENT_INITIATED = "payment_initiated"
    PAYMENT_PROCESSED = "payment_processed"
    PAYMENT_FAILED = "payment_failed"
    SETTLED = "settled"


class PaymentStatus(str, Enum):
    INITIATED = "payment_initiated"
    PROCESSED = "payment_processed"
    FAILED = "payment_failed"


class SettlementStatus(str, Enum):
    PENDING = "pending"
    SETTLED = "settled"