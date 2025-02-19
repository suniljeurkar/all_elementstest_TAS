import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope = "function")
def browser_settings(playwright:Playwright):
    browser = playwright.chromium.launch(headless= False, args =["--start-maximized"])
    context = browser.new_context(no_viewport= True )
    page = context.new_page()

    yield page, context , browser
    context.close()
    browser.close()

