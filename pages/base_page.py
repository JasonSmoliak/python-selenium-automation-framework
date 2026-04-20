from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def load(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_until_not_visible(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_until_present(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_until_enabled(self, locator):
        return self.wait.until(
            lambda d: d.find_element(*locator).is_enabled()
        )

    def wait_until_disabled(self, locator):
        return self.wait.until(
            lambda d: not d.find_element(*locator).is_enabled()
        )

    def click(self, locator):
        element = self.wait_until_clickable(locator)
        element.click()

    def get_text(self, locator):
        return self.wait_until_visible(locator).text

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def type(self, locator, text):
        self.wait_until_visible(locator).send_keys(text)

    def clear_and_type(self, locator, text):
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(text)

    def select_by_text(self, locator, text):
        select = Select(self.wait_until_visible(locator))
        select.select_by_visible_text(text)

    def get_elements(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def log_info(self, message):
        print(f"[INFO] {message}")

    def log_pass(self, message):
        print(f"[PASS] {message}")

    def log_error(self, message):
        print(f"[ERROR] {message}")
