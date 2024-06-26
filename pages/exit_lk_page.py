from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.data import LOGIN, PASSWORD
from tests.urls import URL_LOGIN

email_selector = (By.XPATH, '//input[@name="name"]')
password_selector = (By.XPATH, '//input[@name="Пароль"]')
button_selector = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/button")
button_lk_selector = (By.XPATH, "//a[contains(p/text(),'Личный Кабинет')]")
logaut_selector = (By.XPATH, "//button[text()='Выход']")


class ExitLkPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Метод для открытия страницы
    def open(self):
        self.browser.get(URL_LOGIN)

    # Метод возвращает локатор инпута "email"
    def authorization_email(self):
        return self.find_element(*email_selector)

    # Метод возвращает локатор инпута "Пароль"
    def authorization_password(self):
        return self.find_element(*password_selector)

    # Метод возвращает локатор кнопки "Войти"
    def login_button(self):
        return self.find_element(*button_selector)

    # Метод возвращает локатор кнопки "Личный кабинет"
    def button_lk(self):
        return self.find_element(*button_lk_selector)

    # Метод возвращает локатор кнопки "Выход"
    def logaut(self):
        return self.find_element(*logaut_selector)

    # Метод вписывает данные в форму, используя локаторы полученные в других методах
    def send_keys_authorization(self):
        self.authorization_email().send_keys(LOGIN)
        self.authorization_password().send_keys(PASSWORD)

    # Метод нажимает кнопку "Войти в аккаунт"
    def button_login_click(self):
        self.login_button().click()

    # Метод нажимает кнопку "Личный Кабинет"
    def button_lk_click(self):
        self.button_lk().click()

    # Метод нажимает кнопку "Выход"
    def logout_click(self):
        self.logaut().click()
