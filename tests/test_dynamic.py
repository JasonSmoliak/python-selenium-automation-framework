import pytest
from pages.dynamic_page import DynamicPage


@pytest.mark.ui
def test_remove_and_add_checkbox(driver):
    page = DynamicPage(driver).load()

    page.remove_checkbox()
    assert page.has_checkbox() is False

    page.add_checkbox()
    assert page.has_checkbox() is True


@pytest.mark.ui
def test_enable_disable_input(driver):
    page = DynamicPage(driver).load()

    page.enable_input()
    assert page.is_input_enabled() is True

    page.disable_input()
    assert page.is_input_enabled() is False
