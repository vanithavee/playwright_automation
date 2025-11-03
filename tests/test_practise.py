import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://trytestingthis.netlify.app/")
    page.get_by_role("textbox", name="First name:").click()
    page.get_by_role("textbox", name="First name:").fill("vanitha")
    page.get_by_role("textbox", name="Last name:").click()
    page.get_by_role("textbox", name="Last name:").fill("kumarasamy")
    page.get_by_role("radio", name="Female").check()
    page.locator("#owc").select_option("option 2")
    page.locator("#owc").select_option("option 1")
    page.locator('input[name="option2"]').check()
    page.get_by_role("link", name="Contact").click()
    expect(page.locator("body")).to_match_aria_snapshot(
        '- heading "Your Website to practice Automation Testing" [level=1]'
    )
    page.close()
