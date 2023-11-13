import pytest
from selenium import webdriver

from lib.ui_client import UiClient


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def ui(driver):
    ui_client = UiClient(driver)
    return ui_client
