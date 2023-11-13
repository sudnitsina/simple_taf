from selenium.webdriver.common.by import By

from lib.pages.base_page import BasePage


class AdminPage(BasePage):

    @property
    def header(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div#header")
