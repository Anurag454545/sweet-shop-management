from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_sweets_requires_auth():
    response = client.get("/api/sweets")
    assert response.status_code == 401
