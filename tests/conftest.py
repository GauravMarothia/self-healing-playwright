import pytest
from playwright.sync_api import sync_playwright
from core.healer import PlaywrightHealer

@pytest.fixture(scope="session")
def healer():
    """Initializes the AI Healer once for the entire test session."""
    return PlaywrightHealer()

@pytest.fixture(scope="function")
def browser_context():
    """Sets up a fresh browser instance for every test."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # False to watch the healing
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()