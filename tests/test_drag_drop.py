import pytest
from pages.drag_drop_page import DragDropPage


@pytest.mark.ui
@pytest.mark.xfail(reason="Demo drag-and-drop interaction is unreliable in this environment")
def test_drag_and_drop(driver):
    page = DragDropPage(driver).load()

    before_text = page.target_text
    print("Before drag:", before_text)

    page.drag_to_target()

    after_text = page.target_text
    print("After drag:", after_text)

    assert before_text == "Drop Here"
    assert after_text == "Dropped!"
