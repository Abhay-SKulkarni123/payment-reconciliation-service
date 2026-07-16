from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.event import EventCreateRequest, EventResponse
from app.services.event_service import EventService

router = APIRouter(
    prefix="/events",
    tags=["Events"],
)


@router.post(
    "",
    response_model=EventResponse,
    status_code=201,
)
def ingest_event(
    request: EventCreateRequest,
    db: Session = Depends(get_db),
):
    return EventService.ingest_event(
        db=db,
        event=request,
    )