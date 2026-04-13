from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class FormPage(BasePage):
    URL = "https://practice.expandtesting.com/form-validation"

    CONTACT_NAME = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Contact Name')]/following::input[1]",
    )
    CONTACT_NUMBER = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Contact number')]/following::input[1]",
    )
    PICKUP_DATE = (
        By.XPATH,
        "//label[contains(normalize-space(), 'PickUp Date')]/following::input[1]",
    )
    PAYMENT_METHOD = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Payment Method')]/following::select[1]",
    )
    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Register']")

    def load(self):
        super().load(self.URL)
        return self

    def fill_form(self, contact_name, contact_number, pickup_date, payment_method):
        name_input = self.wait_for_element(self.CONTACT_NAME)
        name_input.clear()
        name_input.send_keys(contact_name)

        number_input = self.wait_for_element(self.CONTACT_NUMBER)
        number_input.clear()
        number_input.send_keys(contact_number)

        date_input = self.wait_for_element(self.PICKUP_DATE)
        date_input.clear()
        date_input.send_keys(pickup_date)

        payment_select = Select(self.wait_for_element(self.PAYMENT_METHOD))
        payment_select.select_by_visible_text(payment_method)

    def submit(self):
        self.click(self.REGISTER_BUTTON)
