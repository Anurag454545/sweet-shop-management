from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_user_can_login_and_get_token():
    # First register the user
    client.post(
        "/api/auth/register",
        json={
            "email": "login@example.com",
            "password": "password123"
        }
    )

    # Then login
    response = client.post(
        "/api/auth/login",
        json={
            "email": "login@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200
    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"
