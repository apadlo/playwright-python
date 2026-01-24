from playwright.sync_api import Playwright, sync_playwright, expect


def test_codegen(playwright: Playwright) -> None:
    # In the terminal type: playwright codegen https://selected_url/
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_text("Switch To Alert Example").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Alert").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="Open Window").click()
    page1 = page1_info.value
    page1.close()
    page.get_by_role("button", name="Hide").click()
    page.get_by_role("button", name="Show").click()
    page.get_by_role("button", name="Mouse Hover").click()
    page.get_by_role("link", name="Top").click()

    # ---------------------
    context.close()
    browser.close()