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
