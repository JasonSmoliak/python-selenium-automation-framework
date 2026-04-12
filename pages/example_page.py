from selenium.webdriver.common.by import By

from components.header_component import HeaderComponent
from components.link_component import LinkComponent
from config.settings import UI_BASE_URL
from pages.base_page import BasePage
from pages.more_info_page import MoreInfoPage


class ExamplePage(BasePage):
    URL = UI_BASE_URL
    MORE_INFO_LINK = (By.CSS_SELECTOR, "a")

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.header = HeaderComponent(driver, timeout)
        self.more_info_link = LinkComponent(driver, self.MORE_INFO_LINK, timeout)

    def load(self):
        super().load(self.URL)
        return self

    @property
    def heading_text(self):
        return self.header.text

    def click_more_info(self):
        self.more_info_link.click()
        return MoreInfoPage(self.driver)
