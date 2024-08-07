import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_health_check():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

@pytest.mark.parametrize("name", ["Alice", "Bob", "Charlie"])
def test_say_hello(name):
    response = client.get(f"/hello/{name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {name}"}
    