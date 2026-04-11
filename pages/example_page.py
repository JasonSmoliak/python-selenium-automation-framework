from selenium.webdriver.common.by import By

from config.settings import UI_BASE_URL
from pages.base_page import BasePage
from pages.more_info_page import MoreInfoPage


class ExamplePage(BasePage):
    URL = UI_BASE_URL

    HEADING = (By.TAG_NAME, "h1")
    MORE_INFO_LINK = (By.CSS_SELECTOR, "a")

    def load(self):
        super().load(self.URL)
        return self

    @property
    def heading_text(self):
        return self.get_text(self.HEADING)

    def click_more_info(self):
        self.click(self.MORE_INFO_LINK)
        return MoreInfoPage(self.driver)
