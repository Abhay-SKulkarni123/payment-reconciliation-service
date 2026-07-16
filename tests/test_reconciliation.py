from .conftest import client

def test_summary():
    response = client.get("/reconciliation/summary")
    assert response.status_code == 200

def test_discrepancies():
    response = client.get("/reconciliation/discrepancies")
    assert response.status_code == 200