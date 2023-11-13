from lib.pages.login_page import LoginPage


class UiClient:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
