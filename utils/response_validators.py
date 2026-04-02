def is_valid_response(response):
    items = response.get("data", {}).get("items", [])
    return response.get("status") in (200, 201) and len(items) > 0

def find_missing_titles(data):
    return [item for item in data if "title" not in item]

def find_missing_keys(data, required_keys):
    if not isinstance(data, list):
        return []

    missing_items = []

    for item in data:
        if not isinstance(item, dict):
            missing_items.append(item)
            continue

        for key in required_keys:
            if key not in item:
                missing_items.append(item)
                break

    return missing_items

def get_nested_value(data, keys):
    current = data

    for key in keys:
        if not isinstance(current, dict):
            return None
        if key not in current:
            return None
        current = current[key]

    return current

def has_nested_value(data, keys):
    return get_nested_value(data, keys) is not None

def is_valid_error_response(response):
    if response.status_code != 404:
        return False

    try:
        data = response.json()
    except Exception:
        return False

    return isinstance(data, dict)

def matches_expected_fields(actual, expected):
    for key, value in expected.items():
        if actual.get(key) != value:
            return False
    return True

def deep_compare_dicts(actual, expected):
    for key in expected:
        if key not in actual:
            return False
        if actual[key] != expected[key]:
            return False
    return True
