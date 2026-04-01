import pytest
from api_client import get
from jsonschema import validate
from schemas.post_schema import POST_SCHEMA
from test_data.api_data import API_SUCCESS_CASES, API_NEGATIVE_CASES
from utils.api_helpers import assert_status, is_json
from utils.response_validators import find_missing_titles
from utils.response_validators import find_missing_keys
from utils.response_validators import get_nested_value
from utils.response_validators import is_valid_error_response
from utils.response_validators import matches_expected_fields
import json

def load_post_test_cases():
    data = load_test_data("test_data/posts.json")
    return [(item["post_id"], item["expected"]) for item in data]

def load_test_data(file_path):
    with open(file_path) as f:
        return json.load(f)

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

@pytest.mark.api
def test_invalid_post_response():
    response = get("/posts/999999")

    assert is_valid_error_response(response)

@pytest.mark.api
def test_all_posts_have_valid_structure_and_types():
    response = get("/posts")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    required_keys = ["userId", "id", "title", "body"]
    missing = find_missing_keys(data, required_keys)

    assert len(missing) == 0, f"Posts missing required fields: {missing}"

    for item in data:
        assert isinstance(item["userId"], int), f"userId is not int: {item}"
        assert isinstance(item["id"], int), f"id is not int: {item}"
        assert isinstance(item["title"], str), f"title is not str: {item}"
        assert isinstance(item["body"], str), f"body is not str: {item}"
        assert item["id"] > 0, f"id must be positive: {item}"

    ids = [item["id"] for item in data]
    assert len(ids) == len(set(ids)), "Duplicate IDs found in response"

@pytest.mark.api
def test_post_1_expected_values():
    response = get("/posts/1")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    expected = {
        "id": 1,
        "userId": 1
    }

    assert matches_expected_fields(data, expected)

import pytest

@pytest.mark.api
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_multiple_posts_have_valid_ids(post_id):
    response = get(f"/posts/{post_id}")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    assert data["id"] == post_id
    assert isinstance(data["userId"], int)

@pytest.mark.api
@pytest.mark.parametrize("post_id, expected_user_id", [
    (1, 1),
    (2, 1),
    (3, 1),
])
def test_posts_expected_user_ids(post_id, expected_user_id):
    response = get(f"/posts/{post_id}")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    assert data["id"] == post_id
    assert data["userId"] == expected_user_id

@pytest.mark.api
@pytest.mark.parametrize("post_id, expected", [
    (1, {"id": 1, "userId": 1}),
    (2, {"id": 2, "userId": 1}),
    (3, {"id": 3, "userId": 1}),
])
def test_posts_match_expected_fields(post_id, expected):
    response = get(f"/posts/{post_id}")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    assert matches_expected_fields(data, expected)

@pytest.mark.api
def test_posts_from_json_data():
    test_data = load_test_data("test_data/posts.json")

    for item in test_data:
        post_id = item["post_id"]
        expected = item["expected"]

        response = get(f"/posts/{post_id}")

        assert_status(response, 200)
        assert is_json(response)

        data = response.json()

        assert matches_expected_fields(data, expected)


@pytest.mark.api
@pytest.mark.parametrize("post_id, expected", load_post_test_cases())
def test_posts_from_json_parametrized(post_id, expected):
    response = get(f"/posts/{post_id}")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    assert matches_expected_fields(data, expected)
