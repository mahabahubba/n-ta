from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_protected_route():
    # Register a unique user
    import time
    ts = int(time.time())
    test_user = {"email": f"user{ts}@example.com", "password": "password123"}
    register_res = client.post("/api/register", json=test_user)
    assert register_res.status_code == 200

    # Login to get token
    login_res = client.post("/api/login", json=test_user)
    assert login_res.status_code == 200
    token = login_res.json()["access_token"]

    # Access protected route with token
    headers = {"Authorization": f"Bearer {token}"}
    protected_res = client.get("/api/me", headers=headers)
    assert protected_res.status_code == 200
    data = protected_res.json()
    assert data["email"] == test_user["email"]

    # Access protected route without token
    unauthorized_res = client.get("/api/me")
    assert unauthorized_res.status_code == 401
