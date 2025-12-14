from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_token():
    client.post(
        "/api/auth/register",
        json={"email": "sweet@test.com", "password": "test123"}
    )
    res = client.post(
        "/api/auth/login",
        json={"email": "sweet@test.com", "password": "test123"}
    )
    return res.json()["access_token"]


def test_add_and_purchase_sweet():
    token = get_token()

    # Add sweet
    res = client.post(
        "/api/sweets",
        json={
            "name": "Kaju Katli",
            "price": 50,
            "quantity": 10
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    sweet_id = res.json()["id"]

    # Purchase sweet
    response = client.post(
        f"/api/sweets/{sweet_id}/purchase",
        json={"quantity": 3},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["quantity"] == 7
