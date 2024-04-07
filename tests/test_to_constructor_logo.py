import time
from pages.constructor_page import ConstructorPage


def test_to_constructor_logo(browser):
    # создал объект класса
    login_page = ConstructorPage(browser)
    # Открываем страницу
    login_page.open_logo_stellar_burgers()

    # Yажимаем кнопку "Личный Кабинет"
    login_page.button_constructor_click()
    time.sleep(1)

    assert browser.current_url == "https://stellarburgers.nomoreparties.site/"
