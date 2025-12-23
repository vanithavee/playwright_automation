from playwright.sync_api import sync_playwright, expect, Page
import pytest
import os


@pytest.fixture(scope="function")
def page_load(page: Page):
    page.goto("https://trytestingthis.netlify.app/")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture(scope="function")
def api_request_context(playwright):

    request_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield request_context
    request_context.dispose()


AUTH = "auth.json"


@pytest.fixture(scope="session")
def auth_state(browser):
    if not os.path.exists(AUTH):
        ctx = browser.new_context()
        page = ctx.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.fill("input[name='username']", "Admin")
        page.fill("input[name='password']", "admin123")
        page.click("button[type='submit']")

        page.wait_for_url("**/dashboard/index")
        ctx.storage_state(path=AUTH)
        ctx.close()

    return AUTH
    # Use the stored authentication state for all tests


@pytest.fixture(scope="function")
def page_with_auth(browser, auth_state):
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()

    yield page

    page.close()
    context.close()
