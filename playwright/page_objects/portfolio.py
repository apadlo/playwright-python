from playwright.sync_api import Page, expect


class PortfolioPage:
    URL = "https://apadlo.streamlit.app/"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def verify_download_button(self) -> None:
        iframe = self.page.locator('iframe[title="streamlitApp"]')
        if iframe.count() > 0:
            root = self.page.frame_locator('iframe[title="streamlitApp"]')
            expect(root.get_by_test_id("stApp")).to_be_visible(timeout=20000)
        else:
            expect(self.page.get_by_test_id("stApp")).to_be_visible(timeout=20000)
