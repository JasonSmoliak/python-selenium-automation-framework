import pytest
from pages.radio_page import RadioPage


@pytest.mark.ui
def test_select_yes_radio(driver):
    page = RadioPage(driver).load()

    page.select_yes()

    assert "Yes" in page.selected_result


@pytest.mark.ui
def test_select_impressive_radio(driver):
    page = RadioPage(driver).load()

    page.select_impressive()

    assert "Impressive" in page.selected_result


@pytest.mark.ui
def test_no_radio_is_disabled(driver):
    page = RadioPage(driver).load()

    assert page.is_no_enabled() is False
