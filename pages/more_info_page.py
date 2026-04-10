from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MoreInfoPage(BasePage):
    HEADING = (By.TAG_NAME, "h1")

    @property
    def heading_text(self):
        return self.get_text(self.HEADING)
