import time

from pages.exit_lk_page import ExitLkPage


def test_logout_button_in_personal_account(browser):
    # создал объект класса
    exit_page = ExitLkPage(browser)
    # Открываем страницу авторизации
    exit_page.open()

    # Авторизуемся
    exit_page.send_keys_authorization()
    exit_page.button_login_click()

    # Заходим в лк и выходим через кнопку "Выход"
    exit_page.button_lk_click()
    exit_page.logout_click()
    time.sleep(2)

    assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"
