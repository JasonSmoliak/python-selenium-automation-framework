from utils.response_validators import find_missing_titles


def test_find_missing_titles_returns_empty_list_when_all_items_are_valid():
    data = [
        {"id": 1, "title": "A"},
        {"id": 2, "title": "B"},
        {"id": 3, "title": "C"},
    ]

    result = find_missing_titles(data)

    assert result == []


def test_find_missing_titles_returns_invalid_items():
    data = [
        {"id": 1, "title": "A"},
        {"id": 2},
        {"id": 3},
    ]

    result = find_missing_titles(data)

    assert len(result) == 2
    assert result == [{"id": 2}, {"id": 3}]
