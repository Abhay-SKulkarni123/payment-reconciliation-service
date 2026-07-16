import json
from pathlib import Path

from app.database import SessionLocal
from app.schemas.event import EventCreateRequest
from app.services.event_service import EventService


def load_events():

    db = SessionLocal()

    file_path = Path("sample_data/sample_events.json")

    with open(file_path, "r") as f:
        events = json.load(f)

    processed = 0

    for event in events:

        request = EventCreateRequest(**event)

        EventService.ingest_event(
            db=db,
            event=request,
        )

        processed += 1

        if processed % 500 == 0:
            print(f"Processed {processed} events...")

    print(f"\nLoaded {processed} events successfully.")


if __name__ == "__main__":
    load_events()