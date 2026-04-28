import pytest

from api_client import get
from schemas.post_schema import POST_SCHEMA
from utils.api_helpers import assert_status, is_json
from utils.schema_validator import validate_schema


@pytest.mark.api
def test_post_response_matches_schema():
    response = get("/posts/1")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    validate_schema(data, POST_SCHEMA)
