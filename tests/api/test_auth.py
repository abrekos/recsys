from dotenv import load_dotenv
from fastapi.testclient import TestClient

health_path = "/health"
load_dotenv()


def test_success_auth(client_with_auth: TestClient, test_bearer_token) -> None:
    with client_with_auth:
        response = client_with_auth.get(health_path, headers={"Authorization": f"Bearer {test_bearer_token}"})
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_no_auth(client_with_auth: TestClient) -> None:
    with client_with_auth:
        response = client_with_auth.get(health_path)
        assert response.status_code == 403


def test_wrong_bearer_token_auth(client_with_auth: TestClient) -> None:
    with client_with_auth:
        response = client_with_auth.get(health_path, headers={"Authorization": "Bearer WRONG_TOKEN"})
        assert response.status_code == 403
