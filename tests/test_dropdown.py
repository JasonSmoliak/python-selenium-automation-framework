import pytest
from pages.dropdown_page import DropdownPage


@pytest.mark.ui
def test_select_option_1(driver):
    page = DropdownPage(driver).load()

    page.select_option_by_text("Option 1")

    selected = page.get_selected_option()

    print("Selected:", selected)

    assert selected == "Option 1"


@pytest.mark.ui
def test_select_option_2(driver):
    page = DropdownPage(driver).load()

    page.select_option_by_text("Option 2")

    selected = page.get_selected_option()

    print("Selected:", selected)

    assert selected == "Option 2"
