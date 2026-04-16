import pytest
from pages.alerts_page import AlertsPage


@pytest.mark.ui
def test_js_alert(driver):
    page = AlertsPage(driver).load()

    page.trigger_alert()

    text = page.get_alert_text()
    print("Alert text:", text)

    page.accept_alert()

    assert "You successfully clicked an alert" in page.get_result_text()


@pytest.mark.ui
def test_js_confirm_accept(driver):
    page = AlertsPage(driver).load()

    page.trigger_confirm()
    page.accept_alert()

    assert "You clicked: Ok" in page.get_result_text()


@pytest.mark.ui
def test_js_confirm_dismiss(driver):
    page = AlertsPage(driver).load()

    page.trigger_confirm()
    page.dismiss_alert()

    assert "You clicked: Cancel" in page.get_result_text()


@pytest.mark.ui
def test_js_prompt(driver):
    page = AlertsPage(driver).load()

    page.trigger_prompt()
    page.send_text_to_prompt("Jason")

    result = page.get_result_text()
    print("Prompt result:", result)

    assert "Jason" in result
