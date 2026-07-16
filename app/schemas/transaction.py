from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel


class MerchantInfo(BaseModel):
    merchant_id: str
    merchant_name: str


class TransactionItem(BaseModel):
    transaction_id: str

    merchant: MerchantInfo

    amount: Decimal
    currency: str

    payment_status: str
    settlement_status: str

    created_at: datetime


class TransactionListResponse(BaseModel):
    total: int

    page: int

    page_size: int

    items: List[TransactionItem]


class EventHistoryItem(BaseModel):
    event_id: str

    event_type: str

    timestamp: datetime


class TransactionDetailResponse(BaseModel):
    transaction_id: str

    merchant: MerchantInfo

    amount: Decimal

    currency: str

    payment_status: str

    settlement_status: str

    created_at: datetime

    updated_at: datetime

    event_history: List[EventHistoryItem]