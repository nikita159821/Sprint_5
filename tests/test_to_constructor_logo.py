import time
from pages.constructor_page import ConstructorPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.urls import URL_SITE


def test_to_constructor_logo(browser):
    # создал объект класса
    login_page = ConstructorPage(browser)
    # Открываем страницу
    login_page.open()

    #  Нажимаем кнопку "Личный Кабинет"
    login_page.button_constructor_click()

    # Явное ожидание загрузки страницы
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_to_be(URL_SITE))

    assert browser.current_url == URL_SITE
