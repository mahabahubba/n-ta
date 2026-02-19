import pytest
import time
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def test_user():
    return {
        "email": "testuser@example.com",
        "password": "password123"
    }

def test_register_user():
    ts = int(time.time())
    test_user = {
        # Creates a unique email for each test run to avoid conflicts
        "email": f"testuser{ts}@example.com",
        "password": "password123"
    }

    response = client.post("/api/register", json=test_user)
    assert response.status_code == 200  
    data = response.json()
    assert "id" in data
    assert data["email"] == test_user["email"]

def test_login_user(test_user):
    # Ensure the user exists
    client.post("/api/register", json=test_user)

    response = client.post("/api/login", json=test_user)
    assert response.status_code == 200
    data = response.json()

    # Backend returns access_token and token_type
    assert "access_token" in data
    assert "token_type" in data
    assert data["token_type"] == "bearer"

def test_protected_route_requires_auth(test_user):
    # Attempt to access /me without token
    response = client.get("/api/me")
    assert response.status_code == 401  

    # Register and login to get token
    client.post("/api/register", json=test_user)
    login_res = client.post("/api/login", json=test_user)
    token = login_res.json()["access_token"]

    # Access /me with token
    response = client.get("/api/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_user["email"]
