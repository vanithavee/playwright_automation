import pytest
import os
from playwright.sync_api import expect

from playwright.sync_api import sync_playwright, Page


def test_dashboard(page_with_auth):

    page_with_auth.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    )
    # expect(page).to_have_title("OrangeHRM")

    assert page_with_auth.title() == "OrangeHRM"


def test_admin(page_with_auth):
    page_with_auth.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    )
    page_with_auth.get_by_role("link", name="Admin").click()
    page_with_auth.pause()
    page_with_auth.locator("form i").first.click()
    page_with_auth.get_by_role("option", name="Admin").click()

    page_with_auth.get_by_role("textbox", name="Type for hints...").fill("value")
    page_with_auth.locator("form i").nth(1).click()
    page_with_auth.get_by_role("option", name="Enabled").click()
