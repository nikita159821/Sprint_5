import time
from pages.constructor_page import ConstructorPage


def test_personal_account_to_constructor_page(browser):
    # создал объект класса
    login_page = ConstructorPage(browser)
    # Открываем страницу
    login_page.open_constructor()

    # Нажимаем кнопку "Личный Кабинет"
    login_page.button_constructor_click()
    time.sleep(1)

    assert browser.current_url == "https://stellarburgers.nomoreparties.site/"


def test_navigation_to_sauces_section(browser):
    # создал объект класса
    login_page = ConstructorPage(browser)
    # Открываем страницу
    login_page.open_burger()

    # Нажимаем "Соусы"
    login_page.button_constructor_burgers()
    time.sleep(3)
    assert login_page.get_text_sauces() == 'Соусы'


def test_navigation_to_fillings_section(browser):
    # создал объект класса
    login_page = ConstructorPage(browser)
    # Открываем страницу
    login_page.open_burger()

    # Нажимаем "Соусы"
    login_page.button_constructor_burgers_fillings()
    time.sleep(3)
    assert login_page.get_text_fillings() == 'Начинки'


def test_navigation_to_buns_section(browser):
    # создал объект класса
    login_page = ConstructorPage(browser)
    # Открываем страницу
    login_page.open_burger()

    # Нажимаем "Соусы", чтобы потом переключиться на "Булки"
    login_page.button_constructor_burgers_fillings()
    time.sleep(3)

    # Нажимаем на "Булки"
    login_page.button_constructor_burgers_buns()
    assert login_page.get_text_buns() == 'Булки'
