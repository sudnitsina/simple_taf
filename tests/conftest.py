import pytest
from selenium import webdriver

from lib.ui_client import UI_client


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def ui(driver):
    ui_client = UI_client(driver)
    return ui_client
