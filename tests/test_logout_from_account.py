import time

from pages.exit_lk_page import ExitLkPage, logaut_selector
from tests.urls import URL_LOGIN
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBurgerLogout:
    def test_logout_button_in_personal_account(self, browser):
        # создал объект класса
        exit_page = ExitLkPage(browser)
        # Открываем страницу авторизации
        exit_page.open()

        # Авторизуемся
        exit_page.send_keys_authorization()
        exit_page.button_login_click()

        # Заходим в лк и выходим через кнопку "Выход"
        exit_page.button_lk_click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located(logaut_selector))
        exit_page.logout_click()

        # Явное ожидание загрузки страницы
        wait = WebDriverWait(browser, 10)
        wait.until(EC.url_to_be(URL_LOGIN))

        assert browser.current_url == URL_LOGIN
