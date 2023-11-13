from lib.pages.admin_page import AdminPage
from lib.pages.login_page import LoginPage


class UiClient:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.admin_page = AdminPage(driver)
