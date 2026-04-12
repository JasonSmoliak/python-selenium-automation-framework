from pages.base_page import BasePage


class LinkComponent(BasePage):
    def __init__(self, driver, locator, timeout=10):
        super().__init__(driver, timeout)
        self.locator = locator

    def click(self):
        super().click(self.locator)

    @property
    def text(self):
        return self.get_text(self.locator)
