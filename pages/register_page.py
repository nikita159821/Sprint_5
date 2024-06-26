from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.data import NAME_REGISTER, LOGIN_REGISTER, PASSWORD_REGISTER
from tests.urls import URL_REGISTER
from helpers import Helpers

name_selector = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")
email_selector = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")
password_selector = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")
button_selector = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/button")
title_auth = (By.XPATH, "//h2")
password_selector_error = (By.XPATH, "//p[@class='input__error text_type_main-default']")


class RegisterPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    # Метод для открытия страницы
    def open(self):
        self.browser.get(URL_REGISTER)

    # Метод возвращает локатор инпута "Имя"
    def name_register(self):
        return self.find_element(*name_selector)

    # Метод возвращает локатор инпута "email"
    def email_register(self):
        return self.find_element(*email_selector)

    # Метод возвращает локатор инпута "Пароль"
    def password_register(self):
        return self.find_element(*password_selector)

    # Метод возвращает локатор кнопки "Регистрация"
    def button(self):
        return self.find_element(*button_selector)

    # Метод нажимает кнопку "Регистрация" через локатора который вернул прошлый метод
    def click_register_button(self):
        self.button().click()

    # Метод возвращает локатор тайтла "Вход", чтобы определить, что регистрация прошла
    def title_authorization(self):
        return self.find_element(*title_auth)

    # Метод для тайм-аута в ожидании тайтла
    def time_authorization(self, browser):
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(self.title_authorization()))

    # Метод вписывает данные в форму регистрации
    def send_keys_register_button(self):
        user_data = Helpers.correct_user_data_generator()
        self.name_register().send_keys(user_data['name'])
        self.email_register().send_keys(user_data['email'])
        self.password_register().send_keys(user_data['password'])

    # Метод вписывает данные в форму c некорректным паролем, используя локаторы полученные в других методах
    def send_keys_register_error_button(self):
        self.name_register().send_keys(NAME_REGISTER)
        self.email_register().send_keys(LOGIN_REGISTER)
        self.password_register().send_keys(PASSWORD_REGISTER)

    # Метод возвращает локатор ошибки при вводе пароля
    def password_error(self):
        return self.find_element(*password_selector_error)

    # Метод обращается за локатором и получает текст ошибки
    def password_error_text(self):
        error_element = self.password_error()
        return error_element.text
