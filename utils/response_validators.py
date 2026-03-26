def is_valid_response(response):
    items = response.get("data", {}).get("items", [])
    return response.get("status") in (200, 201) and len(items) > 0

def find_missing_titles(data):
    return [item for item in data if "title" not in item]
