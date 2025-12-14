from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_user_can_register():
    response = client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "password": "test123"
        }
    )

    assert response.status_code == 200
    data = response.json()

    assert data["email"] == "test@example.com"
    assert "id" in data
