from selenium.webdriver.common.by import By
from pages.base_page import BasePage

button_lk_selector = (By.XPATH, "//a[contains(p/text(),'Личный Кабинет')]")


class LkPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Метод для открытия страницы
    def open(self):
        self.browser.get('https://stellarburgers.nomoreparties.site/')

    def open_constructor(self):
        self.browser.get('https://stellarburgers.nomoreparties.site/login')

    # Метод возвращает локатор кнопки "Личный кабинет"
    def button_lk(self):
        return self.find_element(*button_lk_selector)

    # Метод нажимает кнопку "Личный Кабинет"
    def button_lk_click(self):
        self.button_lk().click()
