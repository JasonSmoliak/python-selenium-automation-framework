# Python Selenium Automation Framework

![CI](https://github.com/JasonSmoliak/python-selenium-automation-framework/actions/workflows/ci.yml/badge.svg)

A production-style QA automation framework built with:

- Python + pytest
- Selenium (UI testing)
- API testing (requests)
- CI/CD with GitHub Actions
- Structured logging, reporting, and test data management

---

## Key Features

- Page Object Model (POM) for UI automation
- API testing (happy path + negative + schema validation)
- Data-driven testing using pytest parametrization
- Advanced test data management (data builders)
- Configurable environments (dev/staging/prod)
- Parallel test execution (pytest-xdist)
- CI pipeline with smoke vs full test strategy
- HTML reports, logs, and artifacts in CI

---

## Running Tests

```bash
make help
make smoke
make api
make ui
make regression
---

## Project Structure

pages/     # UI Page Object Models
tests/     # UI + API test suites
utils/     # Helpers, assertions, data builders
schemas/   # API schemas
config/    # Environment configuration

## CI/CD

GitHub Actions pipeline includes:

- Smoke tests on pull requests
- Full API + UI tests on push
- Parallel browser execution (Chrome + Edge)

Artifacts available after each run:

- HTML test reports
- Failure screenshots
- Execution logs

## Test Report Example

[API Test Report](./screenshots/api_report.png)

## Why This Project

This project demonstrates how to design a scalable, maintainable QA automation framework with:

- clean architecture
- reusable components
- robust CI/CD integration
- realistic testing strategies used in production environments
