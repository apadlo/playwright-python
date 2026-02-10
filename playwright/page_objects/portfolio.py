from playwright.sync_api import expect

class PortfolioPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://apadlo.streamlit.app/")

    def verify_download_button(self):
        download_button = self.page.locator("iframe[title=\"streamlitApp\"]").content_frame.get_by_test_id("stDownloadButton")
        expect(download_button).to_be_visible(timeout=10000)
