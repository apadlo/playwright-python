from playwright.sync_api import Page, expect


class PortfolioPage:
    URL = "https://apadlo.streamlit.app/"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def app_frame(self):
        return self.page.frame_locator('iframe[title="streamlitApp"]')

    def download_button(self):
        return self.app_frame().get_by_test_id("stDownloadButton")

    def verify_download_button(self) -> None:
        expect(self.download_button()).to_be_visible(timeout=10000)
