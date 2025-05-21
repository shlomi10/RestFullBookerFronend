import time

import allure

from pages.base_page import BasePage

"""
Admin page for Automation in Testing hotel demo 
"""


class AdminPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#doLogin")
        self.room_list = page.locator("[data-testid='roomlisting']")
        self.create_room_btn = page.locator("#createRoom")
        self.room_number_input = page.locator("#roomName")
        self.room_type_select = page.locator("#type")
        self.accessible_checkbox = page.locator("#accessible")
        self.price_input = page.locator("#roomPrice")
        self.first_delete_icon = page.locator(".roomDelete").first
        self.features_checkboxes = page.locator(".features input[type=checkbox]")
        self.save_btn = page.get_by_role("button", name="Save")
        self.room_counter = self.page.locator("[data-testid='roomlisting']")
        self.delete_btns = page.locator("button", has_text="Delete")
        self.edit_btns = page.locator("button", has_text="Edit")

    @allure.step("Login to admin panel")
    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)
        self.expect_url_contains("/admin/rooms")
        self.wait_for_element_to_be_visible_locator(self.create_room_btn)

    @allure.step("Add a new room")
    def add_room(self, number, type, price, features: list = [], accessible=False):
        self.fill(self.room_number_input, number)
        self.select_option(self.room_type_select, type)
        if accessible:
            self.select_option(self.accessible_checkbox, "true")
        self.fill(self.price_input, price)
        for feature in features:
            checkbox = self.page.get_by_label(feature)
            if checkbox.is_visible():
                self.click(checkbox)
        self.click(self.create_room_btn)

    @allure.step("Delete first room")
    def delete_first_room(self):
        self.wait_for_element_to_be_visible_locator(self.first_delete_icon)
        self.click(self.first_delete_icon)

    @allure.step("Check if room with number exists")
    def room_exists(self, number: str) -> bool:
        locator = self.page.locator(f"[data-testid='roomlisting']:has-text('{number}')").first
        self.wait_for_element_to_be_visible_locator(locator)
        return locator.is_visible()

    @allure.step("Edit first room")
    def edit_first_room(self, new_price):
        self.fill(self.price_input, new_price)
        self.click(self.create_room_btn)

    @allure.step("Count rooms")
    def get_room_count(self) -> int:
        self.wait_for_element_to_be_visible_locator(self.room_list.first)
        return self.room_counter.count()

    @allure.step("Select the first room and go to it")
    def go_to_room_by_number(self, number: str):
        locator = self.page.locator(f"[data-testid='roomlisting']:has-text('{number}')").first
        self.wait_for_element_to_be_visible_locator(locator)
        locator.click()

    @allure.step("Get first room number")
    def get_first_room_number(self) -> str:
        return self.room_counter.first.locator("p").first.inner_text()

    @allure.step("Wait until room count is less than")
    def wait_until_room_count_is_less_than(self, original_count: int, timeout: int = 5000):
        start = time.time()
        while time.time() - start < timeout / 1000:
            if self.get_room_count() < original_count:
                return
            time.sleep(0.2)
        raise AssertionError("Room count did not decrease in expected time")
