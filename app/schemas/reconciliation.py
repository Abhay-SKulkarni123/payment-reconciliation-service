from pydantic import BaseModel

from typing import List


class ReconciliationSummaryItem(BaseModel):

    merchant_id: str

    merchant_name: str

    total_transactions: int

    processed: int

    failed: int

    settled: int

    pending_settlement: int


class ReconciliationSummaryResponse(BaseModel):

    items: List[ReconciliationSummaryItem]


class DiscrepancyItem(BaseModel):

    transaction_id: str

    merchant_id: str

    merchant_name: str

    payment_status: str

    settlement_status: str

    discrepancy_reason: str


class DiscrepancyResponse(BaseModel):

    items: List[DiscrepancyItem]