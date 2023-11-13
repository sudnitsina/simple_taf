import os


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = os.getenv("BASE_URL")

    def open(self, path):
        self.driver.get(self.base_url + path)
