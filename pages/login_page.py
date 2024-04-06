from selenium.webdriver.common.by import By
from pages.base_page import BasePage

button_login_selector = (By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]/div/button')
email_selector = (By.XPATH, '//input[@name="name"]')
password_selector = (By.XPATH, '//input[@name="Пароль"]')
button_selector = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/button")
button_lk_selector = (By.XPATH, "//a[contains(p/text(),'Личный Кабинет')]")
button_register_selector = (By.XPATH, "//a[contains(text(),'Войти')]")


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Метод для открытия страницы
    def open(self):
        self.browser.get('https://stellarburgers.nomoreparties.site/')

    def open_register(self):
        self.browser.get('https://stellarburgers.nomoreparties.site/register')

    # Метод возвращает локатор кнопки "Войти в аккаунт"
    def button_login(self):
        return self.find_element(*button_login_selector)

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

    # Метод возвращает локатор кнопки "Войти" на странице регистрации
    def button_register(self):
        return self.find_element(*button_register_selector)

    # Метод вписывает данные в форму, используя локаторы полученные в других методах
    def send_keys_authorization(self):
        self.authorization_email().send_keys('nikita_merkulov7@yandex.ru')
        self.authorization_password().send_keys('test123456')

    # Метод нажимает кнопку "Войти в аккаунт"
    def button_login_click(self):
        self.button_login().click()

    # Метод нажимает кнопку "Войти"
    def button_click(self):
        self.login_button().click()

    # Метод нажимает кнопку "Личный Кабинет"
    def button_lk_click(self):
        self.button_lk().click()

    # Метод нажимает кнопку "Войти" на странице регистрации
    def button_register_click(self):
        self.button_register().click()
