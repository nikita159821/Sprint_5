from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from tests.urls import URL_SITE


def test_login_to_account_main_button(browser):
    # создал объект класса
    login_page = LoginPage(browser)
    # Открываем страницу
    login_page.open()

    # Нажимаем кнопку "Войти в аккаунт"
    login_page.button_login_click()

    # Вводим логин и пароль
    login_page.send_keys_authorization()
    # Нажимаем кнопку "Войти"
    login_page.button_click()

    # Явное ожидание загрузки страницы
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_to_be(URL_SITE))

    assert browser.current_url == URL_SITE


def test_login_to_account_personal_cabinet(browser):
    # создал объект класса
    login_page = LoginPage(browser)
    # Открываем страницу
    login_page.open()

    # Нажимаем "Личный кабинет"
    login_page.button_lk_click()

    # Вводим логин и пароль
    login_page.send_keys_authorization()
    # Нажимаем кнопку "Войти"
    login_page.button_click()

    # Явное ожидание загрузки страницы
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_to_be(URL_SITE))

    assert browser.current_url == URL_SITE


def test_login_to_account_registration_form(browser):
    # создал объект класса
    login_page = LoginPage(browser)
    # Открываем страницу
    login_page.open_register()

    # Нажимаем кнопку "Войти"
    login_page.button_register_click()

    # Вводим логин и пароль
    login_page.send_keys_authorization()
    # Нажимаем кнопку "Войти"
    login_page.button_click()

    # Явное ожидание загрузки страницы
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_to_be(URL_SITE))

    assert browser.current_url == URL_SITE


def test_login_to_account_password_recovery_form(browser):
    # создал объект класса
    login_page = LoginPage(browser)
    # Открываем страницу
    login_page.open_forgot_password()

    # Нажимаем кнопку "Войти"
    login_page.button_forgot_password_click()

    # Вводим логин и пароль
    login_page.send_keys_authorization()
    # Нажимаем кнопку "Войти"
    login_page.button_click()

    # Явное ожидание загрузки страницы
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_to_be(URL_SITE))

    assert browser.current_url == URL_SITE
