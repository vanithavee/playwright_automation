from playwright.sync_api import sync_playwright


def test_sample():
    with sync_playwright() as p:
        # Launch the browser (set headless=False to see it open)
        browser = p.chromium.launch(headless=False)

        # Create a new page
        page = browser.new_page()

        # Go to Google
        page.goto("https://trytestingthis.netlify.app/")

        # Keep browser open for a few seconds so you can see it
        page.wait_for_timeout(5000)
        print("page title", page.title())
        browser.close()
