# ShushuraQAAuto

This is a repository for code examples used in my exercises and projects in test automation.

## Overview

In this repository, you will find:

- Examples of tests for API testing
- Examples of tests for UI testing
- Examples of tests for database testing
- Other useful materials for QA automation

## Repository Structure

- `/config/config.py` - Configuration file.
- `/modules/common/database.py` - Module for working with databases.
- `/modules/ui/page_objects/base_page.py` - Base class for web interface pages.
- `/modules/ui/page_objects/sing_in_page.py` - Sign-in page.
- `/modules/api/clients/github.py` - Client for interacting with the GitHub API.
- `/tests/ui/test_ui.py` - Tests for user interface testing.
- `/tests/ui/test_ui_page_object.py` - Tests for testing pages using the page object pattern.
- `/tests/api/test_api.py` - Tests for API.
- `/tests/api/test_fixtures.py` - Fixtures for API tests.
- `/tests/api/test_github_api.py` - Tests for interacting with the GitHub API.
- `/tests/api/test_http.py` - HTTP request tests.
- `/tests/database/test_database.py` - Tests for databases.
- `become_qa_auto.db` - Test database for writing tests.
- `conftest.py` - Pytest configuration file.
- `pytest.ini` - Pytest configuration file.
