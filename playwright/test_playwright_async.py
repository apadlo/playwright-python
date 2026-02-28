from playwright.sync_api import sync_playwright, expect


def test_async_verify_text_on_page():
    test_url = "https://example.com/"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(test_url)
        expect(page).to_have_url(test_url)

        context.close()
        browser.close()
