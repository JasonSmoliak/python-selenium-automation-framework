from components.header_component import HeaderComponent
from pages.base_page import BasePage


class MoreInfoPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.header = HeaderComponent(driver, timeout)

    @property
    def heading_text(self):
        return self.header.text
