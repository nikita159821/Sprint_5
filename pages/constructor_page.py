from selenium.webdriver.common.by import By
from pages.base_page import BasePage

button_constructor_selector = (By.XPATH, "//p[contains(text(),'Конструктор')]")


class ConstructorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_constructor(self):
        self.browser.get('https://stellarburgers.nomoreparties.site/login')

    # Метод возвращает локатор кнопки "Конструктор"
    def button_constructor(self):
        return self.find_element(*button_constructor_selector)

    # Метод нажимает кнопку "Конструктор"
    def button_constructor_click(self):
        self.button_constructor().click()
