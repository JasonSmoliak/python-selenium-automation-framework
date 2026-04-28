import pytest

from api_client import get
from schemas.post_schema import POST_SCHEMA
from utils.api_helpers import assert_status, is_json
from utils.schema_validator import validate_schema


@pytest.mark.api
@pytest.mark.parametrize(
    "post_id",
    [
        pytest.param(1, id="post-1"),
        pytest.param(2, id="post-2"),
        pytest.param(3, id="post-3"),
    ],
)
def test_post_response_matches_schema(post_id):
    response = get(f"/posts/{post_id}")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    validate_schema(data, POST_SCHEMA)
