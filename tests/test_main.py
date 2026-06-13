from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "CI/CD Test Automation Framework API"
    }


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_services():
    response = client.get("/services")
    assert response.status_code == 200

    data = response.json()
    assert "1" in data
    assert data["1"]["name"] == "auth-service"
    assert data["1"]["status"] == "healthy"


def test_get_existing_service():
    response = client.get("/services/1")
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "auth-service"
    assert data["status"] == "healthy"


def test_get_non_existing_service():
    response = client.get("/services/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Service not found"}