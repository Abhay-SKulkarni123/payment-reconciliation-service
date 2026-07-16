from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db

from app.schemas.reconciliation import (
    ReconciliationSummaryItem,
    ReconciliationSummaryResponse,
    DiscrepancyItem,
    DiscrepancyResponse,
)

router = APIRouter(
    prefix="/reconciliation",
    tags=["Reconciliation"],
)


@router.get(
    "/summary",
    response_model=ReconciliationSummaryResponse,
)
def reconciliation_summary(
    db: Session = Depends(get_db),
):

    rows = crud.get_reconciliation_summary(db)

    items = []

    for row in rows:

        items.append(
            ReconciliationSummaryItem(
                merchant_id=row.merchant_id,
                merchant_name=row.merchant_name,
                total_transactions=row.total_transactions,
                processed=row.processed,
                failed=row.failed,
                settled=row.settled,
                pending_settlement=row.pending_settlement,
            )
        )

    return ReconciliationSummaryResponse(
        items=items
    )


@router.get(
    "/discrepancies",
    response_model=DiscrepancyResponse,
)
def reconciliation_discrepancies(
    db: Session = Depends(get_db),
):

    rows = crud.get_reconciliation_discrepancies(db)

    items = []

    for transaction in rows:

        if (
            transaction.payment_status.value == "payment_processed"
            and
            transaction.settlement_status.value == "pending"
        ):

            reason = "Payment processed but not settled"

        else:

            reason = "Failed payment was settled"

        items.append(

            DiscrepancyItem(

                transaction_id=transaction.transaction_id,

                merchant_id=transaction.merchant.merchant_id,

                merchant_name=transaction.merchant.merchant_name,

                payment_status=transaction.payment_status.value,

                settlement_status=transaction.settlement_status.value,

                discrepancy_reason=reason,

            )

        )

    return DiscrepancyResponse(
        items=items
    )