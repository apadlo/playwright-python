"""
Test for Note Agent application
https://deploy-ai-agent-tau.vercel.app/
"""
from playwright.sync_api import expect


class TestNoteAgent:
    """Test suite for Note Agent - AI-powered note generation application"""

    def test_generate_random_note(self, browser_instance):
        """
        Test: Generate a random note using the Note Agent

        Steps:
        1. Navigate to the Note Agent application
        2. Enter a prompt to generate a random note
        3. Click the Send button
        4. Verify that the note is generated and displayed
        5. Verify that the download link is available
        """
        page = browser_instance

        # Navigate to the application
        page.goto("https://deploy-ai-agent-tau.vercel.app/")

        # Verify page loaded correctly
        expect(page).to_have_title("Note Agent")

        # Locate the textarea input field using role-based locator
        textarea = page.get_by_placeholder("Enter your prompt...")
        expect(textarea).to_be_visible()

        # Enter the prompt
        prompt_text = "Generate a random note"
        textarea.fill(prompt_text)

        # Locate and click the Send button using role-based locator
        send_button = page.get_by_role("button", name="Send")
        expect(send_button).to_be_visible()
        send_button.click()

        # Wait for the response to appear
        # The response div has id="response" and becomes visible after submission
        response_div = page.locator("#response")
        expect(response_div).to_be_visible()

        # Verify that the response contains expected text patterns
        # The response should mention that a note was created
        expect(response_div).to_contain_text("note", ignore_case=True)

        # Verify that the download link is available
        download_link = page.locator("a.download-link")
        expect(download_link).to_be_visible()

        # Verify download link has proper href attribute (starts with /download/)
        href = download_link.get_attribute("href")
        assert href.startswith("/download/"), f"Expected download link to start with /download/, got: {href}"
        assert href.endswith(".txt"), f"Expected download link to end with .txt, got: {href}"

        # Additional verification: check that the download link text contains .txt extension
        expect(download_link).to_contain_text(".txt")



