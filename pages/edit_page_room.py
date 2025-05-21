import allure
from pages.base_page import BasePage

"""
edit room page for Automation in Testing hotel demo 
"""


class EditRoomPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.room_header = page.locator(".room-details h2")
        self.edit_button = page.locator(".btn.btn-outline-primary")
        self.type_label = page.locator("p", has_text="Type:")
        self.price_input = page.locator("#roomPrice")
        self.update_btn = page.locator("#update")
        self.price_label = page.locator("p:has-text('Room price:') span")

    @allure.step("Verify edit room page loaded")
    def is_loaded(self) -> bool:
        return self.room_header.is_visible()

    @allure.step("Click edit button")
    def click_edit(self):
        self.wait_for_element_to_be_visible_locator(self.edit_button)
        self.click(self.edit_button)

    @allure.step("Get current room price")
    def get_price(self) -> str:
        return self.get_text(self.price_label)

    @allure.step("Update room price")
    def update_price(self, new_price: str):
        self.wait_for_element_to_be_visible_and_clickable(self.price_input)
        self.fill(self.price_input, new_price)
        self.click(self.update_btn)
        self.wait_for_element_text(self.price_label, new_price)
