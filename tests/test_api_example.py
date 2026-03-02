import pytest
from api_client import get


@pytest.mark.smoke
def test_example_api_status():
    response = get("/posts/1")

    assert response.status_code == 200
    data = response.json()

    assert "userId" in data
    assert "title" in data

@pytest.mark.regression
def test_example_api_not_found():
    response = get("/posts/999999")

    assert response.status_code == 404
