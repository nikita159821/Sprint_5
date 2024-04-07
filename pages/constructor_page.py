from selenium.webdriver.common.by import By
from pages.base_page import BasePage

button_constructor_selector = (By.XPATH, "//p[contains(text(),'Конструктор')]")
logo_constructor_selector = (By.XPATH, "//a[@href='/']")


class ConstructorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_logo_stellar_burgers(self):
        self.browser.get('https://stellarburgers.nomoreparties.site/login')

    # Метод возвращает локатор логотипа "stellar_burgers"
    def button_constructor_logo(self):
        return self.find_element(*logo_constructor_selector)

    # Метод нажимает кнопку "Конструктор"
    def button_constructor_click(self):
        self.button_constructor_logo().click()
