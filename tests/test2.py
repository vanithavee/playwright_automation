from playwright.sync_api import expect


def test_sample1(page):

    page.goto("https://trytestingthis.netlify.app/")

    page.locator("id=fname").fill("vanitha")
    page.locator('//input[@id="lname"]').fill("kumarasamy")
    page.locator('//input[@id="female"]').check()
    # expect(page.locator('//input[@id="female"]')).toBeChecked

    page.get_by_role("link", name="Contact").click()
    expect(page).to_have_title("Page Title")
