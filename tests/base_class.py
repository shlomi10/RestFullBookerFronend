import os

from dotenv import load_dotenv

from pages.admin_page import AdminPage
from pages.edit_page_room import EditRoomPage
from pages.home_page import HomePage

dot_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils", ".env"))
load_dotenv(dotenv_path=dot_env_path)

class BaseClass:
    def __init__(self, page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")
        self.admin = os.getenv("ADMIN_USER")
        self.pwd = os.getenv("ADMIN_PW")
        self.home_page = HomePage(self.page)
        self.admin_page = AdminPage(self.page)
        self.edit_page_room = EditRoomPage(self.page)