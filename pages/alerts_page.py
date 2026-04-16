from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AlertsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    JS_ALERT = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT = (By.XPATH, "//button[text()='Click for JS Prompt']")

    RESULT = (By.ID, "result")

    def load(self):
        super().load(self.URL)
        return self

    def trigger_alert(self):
        self.click(self.JS_ALERT)

    def trigger_confirm(self):
        self.click(self.JS_CONFIRM)

    def trigger_prompt(self):
        self.click(self.JS_PROMPT)

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def send_text_to_prompt(self, text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def get_result_text(self):
        return self.get_text(self.RESULT)
