from .conftest import client


def test_ingest_event():

    payload = {
        "event_id": "pytest-event-001",
        "event_type": "payment_initiated",
        "transaction_id": "pytest-txn-001",
        "merchant_id": "merchant_test",
        "merchant_name": "PyTest Merchant",
        "amount": 500,
        "currency": "INR",
        "timestamp": "2026-01-08T12:11:58Z"
    }

    response = client.post("/events", json=payload)

    assert response.status_code == 201
    assert response.json()["success"] is True


def test_duplicate_event():

    payload = {
        "event_id": "pytest-duplicate",
        "event_type": "payment_initiated",
        "transaction_id": "pytest-txn-duplicate",
        "merchant_id": "merchant_test",
        "merchant_name": "Merchant",
        "amount": 100,
        "currency": "INR",
        "timestamp": "2026-01-08T12:11:58Z"
    }

    first = client.post("/events", json=payload)
    second = client.post("/events", json=payload)

    assert first.status_code == 201
    assert second.json()["success"] is True