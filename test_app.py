import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    """
    GIVEN a server is running
    WHEN a client sends GET request to index
    THEN response is valid HTML
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data
