from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WindowsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/windows"

    CLICK_HERE_LINK = (By.LINK_TEXT, "Click Here")
    PAGE_HEADING = (By.TAG_NAME, "h3")

    def load(self):
        super().load(self.URL)
        return self

    def open_new_window(self):
        self.click(self.CLICK_HERE_LINK)

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @property
    def page_heading_text(self):
        return self.get_text(self.PAGE_HEADING)
