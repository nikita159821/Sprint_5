from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    driver_browser = webdriver.Chrome()
    driver_browser.implicitly_wait(10)
    return driver_browser
