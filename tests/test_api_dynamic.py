import pytest

from utils.data_builders import PostDataBuilder
from utils.api_client import APIClient
from utils.assertions import SoftAssert


@pytest.mark.api
def test_create_post_with_seeded_data(seeded_data):
    api = APIClient()
    data = PostDataBuilder().build()
    print("Generated data:", data)

    response = api.create_post(
        title=data["title"],
        body=data["body"],
        user_id=data["userId"]
    )

    soft = SoftAssert()

    soft.assert_equals(
        response["title"],
        data["title"],
        f"Expected title '{data['title']}', but got '{response['title']}'"
    )
    soft.assert_equals(
        response["body"],
        data["body"],
        "Expected body to match generated test data"
    )
    soft.assert_equals(
        response["userId"],
        data["userId"],
        f"Expected userId '{data['userId']}', but got '{response['userId']}'"
    )

    soft.assert_all()
