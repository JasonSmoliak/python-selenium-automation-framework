import pytest
from api_client import get
from jsonschema import validate
from schemas.post_schema import POST_SCHEMA
from test_data.api_data import API_SUCCESS_CASES, API_NEGATIVE_CASES
from utils.api_helpers import assert_status, is_json
from utils.response_validators import find_missing_titles
from utils.response_validators import find_missing_keys
from utils.response_validators import get_nested_value

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.parametrize("endpoint, expected_status", API_SUCCESS_CASES)
def test_example_api_success(endpoint, expected_status):
    response = get(endpoint)

    assert_status(response, expected_status)
    assert is_json(response)
    
    data = response.json()

    validate(instance=data, schema=POST_SCHEMA)

@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("endpoint, expected_status", API_NEGATIVE_CASES)
def test_example_api_negative(endpoint, expected_status):
    response = get(endpoint)

    assert_status(response, expected_status)

@pytest.mark.api
def test_all_posts_have_titles():
    response = get("/posts")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    missing = find_missing_titles(data)

    assert len(missing) == 0, f"Posts missing titles: {missing}"

@pytest.mark.api
def test_all_posts_have_required_fields():
    response = get("/posts")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    required_keys = ["id", "title", "userId"]

    missing = find_missing_keys(data, required_keys)

    assert len(missing) == 0, f"Posts missing required fields: {missing}"

@pytest.mark.api
def test_post_has_userid_field():
    response = get("/posts/1")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    user_id = get_nested_value(data, ["userId"])

    assert user_id is not None
    assert isinstance(user_id, int)

@pytest.mark.api
def test_invalid_post_returns_404():
    response = get("/posts/999999")

    assert response.status_code == 404

@pytest.mark.api
def test_invalid_post_response_structure():
    response = get("/posts/999999")

    assert response.status_code == 404

    data = response.json()

    assert isinstance(data, dict)
