import pytest
from playwright.async_api import expect, async_playwright

# pytest-asyncio required to run async tests with pytest
# (or anyio, pytest-tornasync, pytest-trio, pytest-twisted)

@pytest.mark.asyncio
async def test_async_verify_text_on_page():
    test_url = "https://example.com/"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(test_url)
        await expect(page).to_have_url(test_url)