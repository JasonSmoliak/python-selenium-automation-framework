# API Automation Framework (Python + Pytest)

![CI](https://github.com/JasonSmoliak/python-selenium-automation-framework/actions/workflows/ci.yml/badge.svg)

## Overview

This project is a Python-based test automation framework designed for UI and API testing.

It supports:
- Selenium-based UI testing (Page Object Model)
- API testing with reusable client utilities
- Parallel execution with pytest-xdist
- Multi-browser testing (Chrome, Edge)
- Environment-based configuration (dev/staging/prod)
- CI/CD integration with GitHub Actions
- HTML reporting and artifact uploads

The framework is built with scalability, maintainability, and real-world QA practices in mind.

---

## Key Features

- Page Object Model (POM) for UI tests
- Reusable API client for backend validation
- Soft and hard assertion strategies
- Parallel execution with pytest-xdist
- Multi-browser support via configuration
- CI pipeline with matrix builds and artifacts
- Screenshot capture on UI failures
- HTML reporting for test results

---

## Framework Highlights

- API client with retries and timeouts
- Pytest fixtures centralized in `conftest.py`
- Page Object Model with shared `BasePage`
- Reusable UI components (`HeaderComponent`, `LinkComponent`)
- Screenshot capture on UI failure
- Environment-based configuration for API and UI

## Tech Stack

• Python
• Pytest
• Requests
• GitHub Actions (CI)

## Key Capabilities

• Page Object Model (POM) architecture for maintainable UI tests  
• Pytest markers for running targeted suites (UI, API, smoke)  
• GitHub Actions CI pipeline running automated checks on every push  
• Automatic screenshot and HTML capture on test failures  
• Explicit waits and retry logic to reduce flaky UI tests  
• Structured logging for debugging test execution

## Project Structure

```
python-selenium-automation-framework/
│
├── pages/                 # Page Object classes
├── tests/                 # Test files
├── conftest.py            # Pytest fixtures (WebDriver setup)
├── pyproject.toml         # Pytest configuration
├── requirements.txt       # Dependencies
└── README.md
```

## Features

- Reusable WebDriver fixture
- Headless execution ready for CI
- Page Object Model implementation
- Clean pytest structure

## How to Run

## Run Tests

### API Tests
make api

### UI Tests
make ui

### UI Tests (headed)
make ui-headed

### UI Tests (Edge)
make ui-edge

## Example Test Patterns

### Parameterized Test
@pytest.mark.parametrize("post_id", [1, 2, 3])

### JSON-driven Testing
test_data = load_test_data("test_data/posts.json")

### Validation Example
is_valid, missing = validate_required_keys(item, required_keys)
assert is_valid, f"Missing keys: {missing}"

### Generate HTML report
`make report`
Then open:
`open reports/report.html`

## CI (GitHub Actions)

This repository includes a GitHub Actions workflow that runs the full pytest suite automatically on every push and pull request.

## Test Organization

Tests are categorized using pytest markers:

- `smoke`: fast critical checks
- `regression`: broader suite
- `ui`: Selenium browser-based tests
- `api`: API tests using requests + schema validation

Examples:
- Run only UI tests: `make ui`
- Run only API tests: `make api`
- Run smoke suite: `make smoke`

## CI/CD Pipeline

- API and UI tests run in separate jobs  
- UI tests execute in parallel using pytest-xdist  
- Matrix builds run UI tests across Chrome and Edge  
- Pip dependencies are cached for faster execution  

## Reporting

HTML test reports can be generated locally using pytest-html:

- `make report`
- `open reports/report.html`

> Note: `reports/` is gitignored because reports are generated artifacts.

## Flaky Test Mitigation

UI tests may be retried on transient failures using pytest-rerunfailures (limited reruns + small delay). Retries are used as a safety net; root causes are addressed with stable locators, explicit waits, and test isolation.

## Status

Initial framework scaffold complete.
Added Page Object Model scaffold (BasePage + ExamplePage).
Currently expanding framework structure and preparing for API test layer.

## Skills Demonstrated

- API automation with pytest and requests
- Selenium UI automation with Page Object Model
- Reusable fixtures and centralized framework design
- Retry and timeout handling for reliability
- Data-driven testing with JSON and parameterization
- CI-friendly reporting and screenshot capture

## Test Report Example

![API Test Report](screenshots/api_report.png)

## Example Output

Status Code: 201
Response Time: 0.20s
37 passed, 6 deselected

⸻

Author

Jason Smoliak
