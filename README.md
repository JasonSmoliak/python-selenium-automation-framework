# API Automation Framework (Python + Pytest)

![CI](https://github.com/JasonSmoliak/python-selenium-automation-framework/actions/workflows/ci.yml/badge.svg)

## Overview
This project is a Python-based API automation framework built using pytest and requests.

It validates REST API responses using reusable helper functions and scalable test patterns.

---

## Key Features

- ✅ Status code validation
- ✅ JSON response validation
- ✅ Required field validation
- ✅ Missing key detection (with detailed error reporting)
- ✅ Partial and full object comparison
- ✅ Recursive validation for nested JSON
- ✅ Parameterized testing
- ✅ JSON-driven test data
- ✅ Edge case and negative testing
- ✅ CI integration with GitHub Actions

---

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

## Environment Configuration

Create a `.env` file (see `.env.example`) to set environment variables locally:

- `BASE_URL` (UI target)

CI sets environment variables directly in the workflow.

## Running Tests

### Run full test suite
`make test`

### Run smoke tests (UI + API)
`make smoke`

### Run regression tests
`make regression`

### Run UI tests only
`make ui`

### Run API tests only
`make api`

### Run with verbose output
./venv/bin/python -m pytest -m api -vv

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

What This Demonstrates

This project showcases:
• Building a scalable API test framework
• Designing reusable validation logic
• Handling real-world API edge cases
• Structuring tests for maintainability
• Debugging and maintaining CI pipelines

## Example Output

Status Code: 201
Response Time: 0.20s
37 passed, 6 deselected

⸻

Author

Jason Smoliak
