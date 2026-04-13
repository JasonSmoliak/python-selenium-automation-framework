import pytest
from pages.form_page import FormPage


@pytest.mark.ui
@pytest.mark.parametrize(
    "contact_name,contact_number,pickup_date,payment_method",
    [
        ("Jason", "5551234567", "12/31/2026", "cash on delivery"),
        ("Jay", "2095551212", "11/15/2026", "card"),
    ],
)
def test_form_page_accepts_valid_inputs(
    driver, contact_name, contact_number, pickup_date, payment_method
):
    page = FormPage(driver).load()

    page.fill_form(contact_name, contact_number, pickup_date, payment_method)
    page.submit()

    assert "form-validation" in driver.current_url.lower()
