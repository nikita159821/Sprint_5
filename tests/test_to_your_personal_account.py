from pages.lk_page import LkPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.urls import URL_LOGIN


def test_login_to_personal_account_button(browser):
    # создал объект класса
    login_page = LkPage(browser)
    # Открываем страницу
    login_page.open()

    # Нажимаем кнопку "Личный Кабинет"
    login_page.button_lk_click()

    # Явное ожидание загрузки страницы
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_to_be(URL_LOGIN))

    assert browser.current_url == URL_LOGIN
