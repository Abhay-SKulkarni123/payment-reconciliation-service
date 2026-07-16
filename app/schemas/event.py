from datetime import datetime
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from app.enums import EventType


class EventCreateRequest(BaseModel):
    event_id: str = Field(..., min_length=1)
    event_type: EventType

    transaction_id: str = Field(..., min_length=1)

    merchant_id: str = Field(..., min_length=1)

    merchant_name: str = Field(..., min_length=1)

    amount: Decimal = Field(..., gt=0)

    currency: str = Field(..., min_length=3, max_length=3)

    timestamp: datetime

    model_config = ConfigDict(
        extra="allow",
        json_schema_extra={
            "example": {
                "event_id": "b768e3a7-9eb3-4603-b21c-a54cc95661bc",
                "event_type": "payment_initiated",
                "transaction_id": "2f86e94c-239c-4302-9874-75f28e3474ee",
                "merchant_id": "merchant_2",
                "merchant_name": "FreshBasket",
                "amount": 15248.29,
                "currency": "INR",
                "timestamp": "2026-01-08T12:11:58.085567+00:00"
            }
        }
    )


class EventResponse(BaseModel):
    success: bool
    message: str
    transaction_id: str