import pytest
from pages.table_page import TablePage


@pytest.mark.ui
def test_table_has_expected_data(driver):
    page = TablePage(driver).load()

    data = page.get_table_data()

    print(data)

    assert len(data) == 4

    last_names = [row[0] for row in data]
    assert "Smith" in last_names
    assert "Doe" in last_names

    emails = [row[2] for row in data]
    assert any("@" in email for email in emails)

    amounts = [row[3] for row in data]
    assert all("$" in amount for amount in amounts)

@pytest.mark.ui
def test_table_sort_by_last_name(driver):
    page = TablePage(driver).load()

    page.sort_by_last_name()

    data = page.get_table_data()
    last_names = [row[0] for row in data]

    expected_names = sorted(last_names)

    print("Actual:", last_names)
    print("Expected:", expected_names)

    assert last_names == expected_names, (
        f"Expected sorted names {expected_names}, got {last_names}"
    )

@pytest.mark.ui
@pytest.mark.parametrize(
    "search_term, expected_last_name",
    [
        ("Smith", "Smith"),
        ("Doe", "Doe"),
        ("Con", "Conway"),
    ],
)
def test_table_filter_by_last_name(driver, search_term, expected_last_name):
    page = TablePage(driver).load()

    filtered_rows = page.filter_rows_by_last_name(search_term)

    print("Filtered rows:", filtered_rows)

    assert len(filtered_rows) > 0, f"No rows found for search term '{search_term}'"

    last_names = [row[0] for row in filtered_rows]
    assert any(expected_last_name == name for name in last_names), (
        f"Expected last name '{expected_last_name}' not found in {last_names}"
    )
