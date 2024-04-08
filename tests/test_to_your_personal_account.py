import time
from pages.lk_page import LkPage


def test_login_to_personal_account_button(browser):
    # создал объект класса
    login_page = LkPage(browser)
    # Открываем страницу
    login_page.open()

    # Нажимаем кнопку "Личный Кабинет"
    login_page.button_lk_click()
    time.sleep(2)

    assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"
