import pytest

from utils.data_generator import random_post_data
from utils.api_client import APIClient
from utils.assertions import assert_equals

@pytest.mark.api
def test_create_post_with_seeded_data(seeded_data):
    api = APIClient()

    data = random_post_data()

    print("Generated data:", data)

    response = api.create_post(
        title=data["title"],
        body=data["body"],
        user_id=data["userId"]
    )

    assert response["title"] == data["title"]
    assert response["body"] == data["body"]
    assert response["userId"] == data["userId"]
