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
