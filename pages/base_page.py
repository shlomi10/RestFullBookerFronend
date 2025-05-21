from playwright.sync_api import Page, Locator, expect
import re


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, element: Locator):
        """Click an element (expects a Locator)."""
        element.click()

    def fill(self, element: Locator, text: str):
        """Fill an input field (expects a Locator)."""
        element.fill(text)

    def get_text(self, element: Locator) -> str:
        """Get the text content of an element (expects a Locator)."""
        return element.inner_text()

    def is_visible(self, element: Locator) -> bool:
        """Check if an element is visible (expects a Locator)."""
        return element.is_visible()

    def wait_for_element_to_be_visible_locator(self, element: Locator, timeout: int = 5000):
        """Wait for an element to be visible (expects a locator)."""
        expect(element).to_be_visible(timeout=timeout)

    def wait_for_element_to_be_visible_and_clickable(self, element: Locator, timeout: int = 5000):
        """Wait for an element to be visible and clickable (expects a locator)."""
        expect(element).to_be_visible(timeout=timeout)
        expect(element).to_be_enabled(timeout=timeout)

    def expect_url_contains(self, chunk: str, timeout: int = 5_000):
        """Wait for page to contain url."""
        pattern = re.compile(f".*{re.escape(chunk)}.*")
        expect(self.page).to_have_url(pattern, timeout=timeout)

    def select_option(self, element: Locator, value: str):
        """Select an option from a dropdown (expects a Locator)."""
        element.select_option(value)

    def wait_for_element_text(self, element: Locator, expected_text: str, timeout: int = 6000):
        """wait for an element to have a specific text."""
        expect(element).to_have_text(expected_text, timeout=timeout)
