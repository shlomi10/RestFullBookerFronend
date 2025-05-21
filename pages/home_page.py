import allure

from pages.base_page import BasePage

"""
Landing page for Automation in Testing hotel demo 
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("home page")
class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.welcome_message = page.locator("h1.display-4")
        self.admin_link = page.get_by_role("link", name="Admin", exact=True)
        self.create_btn = page.locator("#createRoom")

    @allure.step("wait for home page")
    def wait_for_home_page(self) -> None:
        self.wait_for_element_to_be_visible_locator(self.welcome_message)

    @allure.step("Go to admin panel")
    def open_admin(self):
        self.click(self.admin_link)
        self.expect_url_contains("/admin")

    @allure.step("Verify landing page loaded")
    def is_loaded(self) -> bool:
        return self.is_visible(self.create_btn)
