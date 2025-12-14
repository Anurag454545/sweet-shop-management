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


def test_get_sweets_requires_auth():
    response = client.get("/api/sweets")
    assert response.status_code == 401


def test_add_sweet_success():
    token = get_token()

    response = client.post(
        "/api/sweets",
        json={
            "name": "Ladoo",
            "price": 10,
            "quantity": 100
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Ladoo"


def test_search_sweets():
    token = get_token()

    client.post(
        "/api/sweets",
        json={
            "name": "Jalebi",
            "price": 15,
            "quantity": 50
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    response = client.get(
        "/api/sweets/search?query=Jalebi",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()[0]["name"] == "Jalebi"


def test_update_sweet():
    token = get_token()

    res = client.post(
        "/api/sweets",
        json={
            "name": "Barfi",
            "price": 20,
            "quantity": 30
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    sweet_id = res.json()["id"]

    response = client.put(
        f"/api/sweets/{sweet_id}",
        json={
            "name": "Barfi Special",
            "price": 25,
            "quantity": 40
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Barfi Special"


def test_delete_sweet():
    token = get_token()

    # Create sweet
    res = client.post(
        "/api/sweets",
        json={
            "name": "Peda",
            "price": 12,
            "quantity": 20
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    sweet_id = res.json()["id"]

    # Delete sweet
    response = client.delete(
        f"/api/sweets/{sweet_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["detail"] == "Sweet deleted"
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


def test_get_sweets_requires_auth():
    response = client.get("/api/sweets")
    assert response.status_code == 401


def test_add_sweet_success():
    token = get_token()

    response = client.post(
        "/api/sweets",
        json={
            "name": "Ladoo",
            "price": 10,
            "quantity": 100
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Ladoo"


def test_search_sweets():
    token = get_token()

    client.post(
        "/api/sweets",
        json={
            "name": "Jalebi",
            "price": 15,
            "quantity": 50
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    response = client.get(
        "/api/sweets/search?query=Jalebi",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()[0]["name"] == "Jalebi"


def test_update_sweet():
    token = get_token()

    res = client.post(
        "/api/sweets",
        json={
            "name": "Barfi",
            "price": 20,
            "quantity": 30
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    sweet_id = res.json()["id"]

    response = client.put(
        f"/api/sweets/{sweet_id}",
        json={
            "name": "Barfi Special",
            "price": 25,
            "quantity": 40
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Barfi Special"


def test_delete_sweet():
    token = get_token()

    # Create sweet
    res = client.post(
        "/api/sweets",
        json={
            "name": "Peda",
            "price": 12,
            "quantity": 20
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    sweet_id = res.json()["id"]

    # Delete sweet
    response = client.delete(
        f"/api/sweets/{sweet_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["detail"] == "Sweet deleted"
