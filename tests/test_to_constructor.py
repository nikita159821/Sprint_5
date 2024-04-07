import time
from pages.constructor_page import ConstructorPage


def test_personal_account_to_constructor_page(browser):
    # создал объект класса
    login_page = ConstructorPage(browser)
    # Открываем страницу
    login_page.open_constructor()

    # Yажимаем кнопку "Личный Кабинет"
    login_page.button_constructor_click()
    time.sleep(1)

    assert browser.current_url == "https://stellarburgers.nomoreparties.site/"
