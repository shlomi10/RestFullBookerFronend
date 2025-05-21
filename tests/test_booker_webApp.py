import allure
import pytest
import random
import logging

log = logging.getLogger(__name__)
room_types = ["Single", "Twin", "Double", "Family", "Suite"]
features_pool = ["WiFi", "TV", "Radio", "Refreshments", "Safe", "Views"]


def login_to_admin(initialize):
    log.info("Logging into admin panel")
    initialize.home_page.wait_for_home_page()
    initialize.home_page.open_admin()
    initialize.admin_page.login(initialize.admin, initialize.pwd)
    initialize.home_page.is_loaded()
    log.info("Successfully logged in")


@allure.epic("Functionality")
@allure.feature("Room Management")
@allure.story("Validate the Restful Booker WebApp functionality")
class TestRestfulBookerWebApp:

    @allure.title("Add Room with dynamic data")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("accessible", [True, False], ids=["accessible", "not_accessible"])
    @pytest.mark.parametrize("room_type", room_types, ids=lambda rt: f"type={rt}")
    def test_add_room(self, initialize, room_type, accessible):
        with allure.step("Navigate and login"):
            log.info("Starting test_add_room")
            login_to_admin(initialize)

        room_number = str(random.randint(100, 999))
        price = str(random.randint(100, 995))
        features = random.sample(features_pool, k=random.randint(1, 6))
        log.info(
            f"Generated room_number={room_number}, type={room_type}, price={price}, "
            f"accessible={accessible}, features={features}"
        )

        with allure.step(f"Add room {room_number}"):
            log.info(f"Adding room {room_number}")
            initialize.admin_page.add_room(
                number=room_number,
                type=room_type,
                price=price,
                features=features,
                accessible=accessible
            )

        with allure.step("Verify room was created"):
            log.info("Verifying room existence in admin panel")
            assert initialize.admin_page.room_exists(room_number), "The room was not created in the admin panel"
            log.info("test_add_room completed successfully")

    @allure.title("Update first room")
    @pytest.mark.flaky(reruns=1)
    def test_update_room(self, initialize):
        log.info("Starting test_update_room")
        login_to_admin(initialize)

        with allure.step("Navigate to first room details"):
            first_room_number = initialize.admin_page.get_first_room_number()
            log.info(f"Navigated to room {first_room_number}")
            initialize.admin_page.go_to_room_by_number(first_room_number)

        initialize.edit_page_room.is_loaded()
        initialize.edit_page_room.click_edit()

        new_price = "999"
        log.info(f"Updating room price to {new_price}")
        initialize.edit_page_room.update_price(new_price)

        with allure.step("Assert price updated"):
            actual_price = initialize.edit_page_room.get_price()
            log.info(f"New price on page: {actual_price}")
            assert str(actual_price) == new_price, f"Expected price '{new_price}', got '{actual_price}'"
            log.info("test_update_room completed successfully")

    @allure.title("Delete first room")
    @pytest.mark.flaky(reruns=1)
    def test_delete_room(self, initialize):
        log.info("Starting test_delete_room")
        login_to_admin(initialize)

        with allure.step("Count rooms before delete"):
            before = initialize.admin_page.get_room_count()
            log.info(f"Room count before delete: {before}")

        initialize.admin_page.delete_first_room()

        with allure.step("Assert room was deleted"):
            initialize.admin_page.wait_until_room_count_is_less_than(before)
            after = initialize.admin_page.get_room_count()
            log.info(f"Room count after delete: {after}")
            assert after == before - 1, "The room was not deleted from the admin panel"
            log.info("test_delete_room completed successfully")
