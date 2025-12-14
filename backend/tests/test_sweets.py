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


def test_restock_sweet():
    token = get_token()

    # Create sweet
    res = client.post(
        "/api/sweets",
        json={
            "name": "Rasgulla",
            "price": 30,
            "quantity": 5
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    sweet_id = res.json()["id"]

    # Restock sweet
    response = client.post(
        f"/api/sweets/{sweet_id}/restock",
        json={"quantity": 10},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["quantity"] == 15
