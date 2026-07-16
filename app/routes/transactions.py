from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas.transaction import (
    EventHistoryItem,
    MerchantInfo,
    TransactionDetailResponse,
    TransactionItem,
    TransactionListResponse,
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


ALLOWED_SORT_FIELDS = {
    "created_at",
    "amount",
    "payment_status",
}


@router.get(
    "",
    response_model=TransactionListResponse,
)
def list_transactions(
    merchant_id: str | None = None,
    payment_status: str | None = None,
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
    sort_by: str = Query(default="created_at"),
    sort_order: str = Query(default="desc"),
    db: Session = Depends(get_db),
):

    if sort_by not in ALLOWED_SORT_FIELDS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort_by. Allowed values: {', '.join(ALLOWED_SORT_FIELDS)}",
        )

    if sort_order.lower() not in {"asc", "desc"}:
        raise HTTPException(
            status_code=400,
            detail="sort_order must be either 'asc' or 'desc'",
        )

    total, transactions = crud.list_transactions(
        db=db,
        merchant_id=merchant_id,
        payment_status=payment_status,
        start_date=start_date,
        end_date=end_date,
        page=page,
        page_size=page_size,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    items = []

    for transaction in transactions:

        items.append(
            TransactionItem(
                transaction_id=transaction.transaction_id,
                merchant=MerchantInfo(
                    merchant_id=transaction.merchant.merchant_id,
                    merchant_name=transaction.merchant.merchant_name,
                ),
                amount=transaction.amount,
                currency=transaction.currency,
                payment_status=transaction.payment_status.value,
                settlement_status=transaction.settlement_status.value,
                created_at=transaction.created_at,
            )
        )

    return TransactionListResponse(
        total=total,
        page=page,
        page_size=page_size,
        items=items,
    )


@router.get(
    "/{transaction_id}",
    response_model=TransactionDetailResponse,
)
def get_transaction(
    transaction_id: str,
    db: Session = Depends(get_db),
):

    transaction = crud.get_transaction_details(
        db=db,
        transaction_id=transaction_id,
    )

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found",
        )

    events = []

    for event in transaction.events:

        events.append(
            EventHistoryItem(
                event_id=event.event_id,
                event_type=event.event_type.value,
                timestamp=event.event_timestamp,
            )
        )

    return TransactionDetailResponse(
        transaction_id=transaction.transaction_id,
        merchant=MerchantInfo(
            merchant_id=transaction.merchant.merchant_id,
            merchant_name=transaction.merchant.merchant_name,
        ),
        amount=transaction.amount,
        currency=transaction.currency,
        payment_status=transaction.payment_status.value,
        settlement_status=transaction.settlement_status.value,
        created_at=transaction.created_at,
        updated_at=transaction.updated_at,
        event_history=events,
    )