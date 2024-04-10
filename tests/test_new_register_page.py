import time

from pages.register_page import RegisterPage


def test_register_page(browser):
    # создал объект класса
    register_page = RegisterPage(browser)
    # Открываем страницу регистрации
    register_page.open()

    # Вводим все данные
    register_page.send_keys_register_button()
    # Нажимаем на кнопку "Регистрация"
    register_page.click_register_button()

    # После авториации появляется форма фхода. Проверяем тайтл "Вход", если есть,
    # значит тест пройден, регистрация завершена"
    assert register_page.title_authorization().is_displayed()


def test_register_error_password(browser):
    # создал объект класса
    register_page = RegisterPage(browser)
    # Открываем страницу регистрации
    register_page.open()

    # Вводим все данные
    register_page.send_keys_register_error_button()
    # Нажимаем на кнопку "Регистрация"
    register_page.click_register_button()

    # Сравнимаем полученный текст с ожидаемым.
    assert register_page.password_error_text() == 'Некорректный пароль'
