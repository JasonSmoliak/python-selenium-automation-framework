import pytest
from pages.windows_page import WindowsPage


@pytest.mark.ui
def test_switch_to_new_window(driver):
    page = WindowsPage(driver).load()

    original_window = driver.current_window_handle
    print("Original window:", original_window)

    page.open_new_window()

    all_windows = page.get_window_handles()
    print("All windows:", all_windows)

    assert len(all_windows) == 2, f"Expected 2 windows, got {len(all_windows)}"

    new_window = [handle for handle in all_windows if handle != original_window][0]
    page.switch_to_window(new_window)

    heading = page.page_heading_text
    print("New window heading:", heading)

    assert heading == "New Window", f"Expected 'New Window', got '{heading}'"


@pytest.mark.ui
def test_switch_back_to_original_window(driver):
    page = WindowsPage(driver).load()

    original_window = driver.current_window_handle
    page.open_new_window()

    all_windows = page.get_window_handles()
    new_window = [handle for handle in all_windows if handle != original_window][0]

    page.switch_to_window(new_window)
    assert page.page_heading_text == "New Window"

    page.switch_to_window(original_window)
    assert page.page_heading_text == "Opening a new window"
