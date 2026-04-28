from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ModalPage(BasePage):
    URL = "https://the-internet.herokuapp.com/entry_ad"

    MODAL = (By.CLASS_NAME, "modal")
    MODAL_TITLE = (By.CSS_SELECTOR, ".modal-title")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".modal-footer p")
    PAGE_HEADING = (By.TAG_NAME, "h3")

    def load(self):
        super().load(self.URL)
        return self

    def wait_for_modal(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.MODAL)
            )
        except TimeoutException:
            return None

    def is_modal_visible(self):
        elements = self.driver.find_elements(*self.MODAL)
        return len(elements) > 0 and elements[0].is_displayed()

    @property
    def modal_title_text(self):
        return self.get_text(self.MODAL_TITLE)

    def close_modal(self):
        if self.is_modal_visible():
            self.click(self.CLOSE_BUTTON)
            self.wait_until_not_visible(self.MODAL)

    @property
    def page_heading_text(self):
        return self.get_text(self.PAGE_HEADING)
