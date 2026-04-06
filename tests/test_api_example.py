import pytest
import json

from api_client import get, post, delete, put
from jsonschema import validate
from schemas.post_schema import POST_SCHEMA
from test_data.api_data import API_SUCCESS_CASES, API_NEGATIVE_CASES
from utils.api_helpers import assert_status, is_json
from utils.api_helpers import get_auth_headers
from utils.api_helpers import log_response
from utils.response_validators import (
    deep_compare_dicts,
    find_missing_keys,
    find_missing_titles,
    get_missing_keys,
    get_nested_value,
    has_nested_value,
    is_valid_error_response,
    matches_expected_fields,
    validate_required_keys,
)

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

@pytest.mark.api
def test_post_1_full_validation():
    response = get("/posts/1")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    expected = {
        "id": 1,
        "userId": 1,
        "title": data["title"],
        "body": data["body"]
    }

    assert deep_compare_dicts(data, expected)

@pytest.mark.api
def test_missing_required_fields_fails():
    bad_data = {
        "id": 1
        # missing userId, title, body
    }

    required_keys = ["userId", "title", "body"]

    missing = find_missing_keys([bad_data], required_keys)

    assert len(missing) == 1

@pytest.mark.api
def test_wrong_data_types_fail():
    bad_data = {
        "id": "1",  # should be int
        "userId": "1",  # should be int
        "title": 123,  # should be str
        "body": []
    }

    assert not isinstance(bad_data["id"], int)
    assert not isinstance(bad_data["userId"], int)
    assert not isinstance(bad_data["title"], str)
    assert not isinstance(bad_data["body"], str)

@pytest.mark.api
def test_empty_response_handling():
    data = []

    assert isinstance(data, list)
    assert len(data) == 0

@pytest.mark.api
def test_validate_required_keys_helper():
    item = {"id": 1}

    required = ["id", "userId"]

    is_valid, missing = validate_required_keys(item, required)

    assert not is_valid
    assert missing == ["userId"]

@pytest.mark.api
def test_get_with_headers():
    headers = {
        "Content-Type": "application/json"
    }

    response = get("/posts/1", headers=headers)

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    assert data["id"] == 1
 
@pytest.mark.api
def test_auth_headers_structure():
    token = "test_token"

    headers = get_auth_headers(token)

    assert "Authorization" in headers
    assert headers["Authorization"] == "Bearer test_token"
    assert headers["Content-Type"] == "application/json"

@pytest.mark.api
def test_missing_auth_header():
    response = get("/posts/1", headers={})

    assert_status(response, 200)  # JSONPlaceholder allows it

@pytest.mark.api
def test_invalid_auth_header():
    headers = get_auth_headers("invalid_token")

    response = get("/posts/1", headers=headers)

    assert_status(response, 200)  # placeholder API behavior

@pytest.mark.api
def test_create_post():
    payload = {
        "title": "test title",
        "body": "test body",
        "userId": 1
    }

    response = post("/posts", json=payload)
    
    assert_status(response, 201)
    assert is_json(response)

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


@pytest.mark.api
def test_delete_post():
    response = delete("/posts/1")

    assert_status(response, 200)

@pytest.mark.api
def test_create_update_delete_workflow():
    # Step 1: Create
    payload = {
        "title": "original title",
        "body": "original body",
        "userId": 1
    }

    create_response = post("/posts", json=payload)
    log_response(create_response)
    assert_status(create_response, 201)

    created = create_response.json()
    assert created["title"] == payload["title"]
    assert created["body"] == payload["body"]
    assert created["userId"] == payload["userId"]

    assert create_response.elapsed.total_seconds() < 2, "Create request too slow"

    # Step 2: Update a known existing resource
    updated_payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }

    update_response = put("/posts/1", json=updated_payload)
    log_response(update_response)
    assert_status(update_response, 200)

    updated = update_response.json()

    expected_update = {
    	"title": "updated title",
    	"body": "updated body",
    	"userId": 1
    }

    assert matches_expected_fields(updated, expected_update)
    required_keys = ["title", "body", "userId"]

    is_valid, missing = validate_required_keys(updated, required_keys)

    assert is_valid, f"Missing keys: {missing}"

    assert update_response.elapsed.total_seconds() < 2, "Update request too slow"

    
    # Step 3: Delete a known existing resource
    delete_response = delete("/posts/1")
    log_response(delete_response)    
    assert delete_response.status_code in (200, 204)
    assert delete_response.elapsed.total_seconds() < 2, "Delete request too slow"


@pytest.mark.api
def test_posts_response_time_under_two_seconds():
    response = get("/posts")

    assert_status(response, 200)

    elapsed = response.elapsed.total_seconds()

    assert elapsed < 2, f"Response took too long: {elapsed:.2f}s"
