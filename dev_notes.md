# Dev Notes (Quick Workflow)

## Run tests
- Activate venv: `source venv/bin/activate`
- Run suite: `python -m pytest -q`
- Run verbose: `python -m pytest`

## Add a new page object
1. Create file in `pages/` (example: `pages/login_page.py`)
2. Inherit from `BasePage`
3. Define locators as tuples: `SOME_LOCATOR = (By.ID, "value")`
4. Use BasePage helpers: `self.get_text(locator)`, `self.click(locator)`, `self.find(locator)`

## Add a new test
1. Create file in `tests/` (example: `tests/test_login.py`)
2. Import your page: `from pages.login_page import LoginPage`
3. Use the fixture: `def test_login(driver): ...`

## Commit + push
- `git status`
- `git add .`
- `git commit -m "Describe change"`
- `git push`
