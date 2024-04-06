import time

from pages.login_page import LoginPage


def test_login_to_account_main_page(browser):
    # создал объект класса
    login_page = LoginPage(browser)

    # Открываем страницу регистрации
    login_page.open()
    # Нажимаем кнопку "Войти в аккаунт"
    login_page.button_login_click()
    # Вводим логин и пароль
    login_page.send_keys_authorization()
    # Нажимаем кнопку "Войти"
    login_page.button_click()
    time.sleep(1)
    assert browser.current_url == "https://stellarburgers.nomoreparties.site/"
