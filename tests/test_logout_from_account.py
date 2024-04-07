import time

from pages.exit_lk_page import ExitLkPage


def test_logout_button_in_personal_account(browser):
    # создал объект класса
    register_page = ExitLkPage(browser)
    # Открываем страницу авторизации
    register_page.open()

    # Авторизуемся
    register_page.send_keys_authorization()
    register_page.button_login_click()

    # Заходим в лк и выходим через кнопку "Выход"
    register_page.button_lk_click()
    register_page.logout_click()
    time.sleep(2)

    assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"
