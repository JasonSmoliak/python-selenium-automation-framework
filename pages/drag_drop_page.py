from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DragDropPage(BasePage):
    URL = "https://demoqa.com/droppable"

    DRAGGABLE = (By.ID, "draggable")
    DROPPABLE = (By.ID, "droppable")

    def load(self):
        super().load(self.URL)
        return self

    def drag_to_target(self):
        source = self.wait_for_element(self.DRAGGABLE)
        target = self.wait_for_element(self.DROPPABLE)

        script = """
        const source = arguments[0];
        const target = arguments[1];

        const dataTransfer = new DataTransfer();

        source.dispatchEvent(new DragEvent('dragstart', {
            dataTransfer: dataTransfer,
            bubbles: true
        }));

        target.dispatchEvent(new DragEvent('drop', {
            dataTransfer: dataTransfer,
            bubbles: true
        }));

        source.dispatchEvent(new DragEvent('dragend', {
            dataTransfer: dataTransfer,
            bubbles: true
        }));
        """

        this_driver = self.driver
        this_driver.execute_script(script, source, target)

    @property
    def target_text(self):
        return self.get_text(self.DROPPABLE)
