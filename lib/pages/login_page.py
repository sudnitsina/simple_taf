from selenium.webdriver.common.by import By

from lib.pages.base_page import BasePage


class LoginPage(BasePage):
    def fill_username(self, name):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(
            name
        )

    def fill_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(
            password
        )

    def click_login_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def login(self, name, password):
        self.open("/login")
        self.fill_username(name)
        self.fill_password(password)
        self.click_login_btn()
