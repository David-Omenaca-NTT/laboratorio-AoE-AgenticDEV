from fastapi.testclient import TestClient

from src.app.main import app, received_names


client = TestClient(app)


def test_health_returns_200():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_hello_valid_returns_200_without_authentication():
    response = client.post("/hello", json={"name": "David"})

    assert response.status_code == 200


def test_hello_returns_expected_message():
    response = client.post("/hello", json={"name": "David"})

    assert response.json() == {"message": "Hello David"}


def test_hello_rejects_empty_name():
    response = client.post("/hello", json={"name": ""})

    assert response.status_code == 422


def test_hello_rejects_whitespace_only_name():
    response = client.post("/hello", json={"name": "   "})

    assert response.status_code == 422


def test_hello_rejects_missing_name():
    response = client.post("/hello", json={})

    assert response.status_code == 422


def test_hello_stores_received_name_in_memory():
    client.post("/hello", json={"name": "David"})

    assert received_names[-1] == "David"
