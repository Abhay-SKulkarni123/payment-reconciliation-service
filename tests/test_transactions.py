from .conftest import client


def test_list_transactions():
    response = client.get("/transactions")
    assert response.status_code == 200
    assert "items" in response.json()


def test_transaction_filter():
    response = client.get("/transactions?merchant_id=merchant_1")
    assert response.status_code == 200


def test_transaction_detail():
    response = client.get("/transactions")
    transaction = response.json()["items"][0]
    txn_id = transaction["transaction_id"]
    detail = client.get(f"/transactions/{txn_id}")
    assert detail.status_code == 200