import requests
import pytest


@pytest.mark.smoke
def test_example_api_status():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200
    data = response.json()

    assert "userId" in data
    assert "title" in data
