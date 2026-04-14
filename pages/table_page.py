from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TablePage(BasePage):
    URL = "https://the-internet.herokuapp.com/tables"

    TABLE_ROWS = (By.CSS_SELECTOR, "#table1 tbody tr")

    def load(self):
        super().load(self.URL)
        return self

    def get_table_data(self):
        rows = self.get_elements(self.TABLE_ROWS)
        table_data = []

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            row_data = [col.text for col in cols]
            table_data.append(row_data)

        return table_data

    LAST_NAME_HEADER = (By.CSS_SELECTOR, "#table1 th:nth-child(1)")

    def sort_by_last_name(self):
        self.click(self.LAST_NAME_HEADER)
