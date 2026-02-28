from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MoreInfoPage(BasePage):
    H1 = (By.TAG_NAME, "h1")

    def heading_text(self):
        return self.get_text(self.H1)
