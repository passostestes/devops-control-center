
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_system():
    response = client.get("/system")
    assert response.status_code == 200

    data = response.json()
    assert "os" in data
    assert "python" in data
