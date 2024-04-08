from selenium import webdriver
import pytest


import sys
import os

# Добавляем путь к директории "pages"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))




@pytest.fixture
def browser():
    driver_browser = webdriver.Chrome()
    driver_browser.implicitly_wait(10)
    yield driver_browser
    return driver_browser

