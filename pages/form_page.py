from selenium.webdriver.common.by import By

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
        self.clear_and_type(self.CONTACT_NAME, contact_name)
        self.clear_and_type(self.CONTACT_NUMBER, contact_number)
        self.clear_and_type(self.PICKUP_DATE, pickup_date)
        self.select_by_text(self.PAYMENT_METHOD, payment_method)

    def submit(self):
        self.click(self.REGISTER_BUTTON)
