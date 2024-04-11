from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.urls import URL_LOGIN, URL_SITE

button_constructor_selector = (By.XPATH, "//p[contains(text(),'Конструктор')]")
logo_constructor_selector = (By.XPATH, "//a[@href='/']")
constructor_burger_selector_1 = (By.XPATH, "//span[text()='Булки']")
constructor_burger_selector_2 = (By.XPATH, "//span[text()='Соусы']")
constructor_burger_selector_3 = (By.XPATH, "//span[text()='Начинки']")

buns = (By.XPATH, "//div[contains(@class,'tab_tab_type_current__2BEPc')]")
sauces = (By.XPATH, "//div[contains(@class,'tab_tab_type_current__2BEPc')]")
fillings = (By.XPATH, "//div[contains(@class,'tab_tab_type_current__2BEPc')]")



class ConstructorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(URL_LOGIN)

    def open_burger(self):
        self.browser.get(URL_SITE)

    # Метод возвращает локатор логотипа "stellar_burgers"
    def button_constructor_logo(self):
        return self.find_element(*logo_constructor_selector)

    # Метод возвращает локатор "Булки"
    def construct_burger_buns(self):
        return self.find_element(*constructor_burger_selector_1)

    # Метод возвращает новый локатор "Булки"
    def buns(self):
        return self.find_element(*buns)

    # Метод возвращает локатор "Соусы"
    def constructor_burgers(self):
        return self.find_element(*constructor_burger_selector_2)

    # Метод возвращает новый локатор "Соусы"
    def sauces(self):
        return self.find_element(*sauces)

    # Метод возвращает локатор "Начинки"
    def constructor_burgers_fillings(self):
        return self.find_element(*constructor_burger_selector_3)

    # Метод возвращает новый локатор "Начинки"
    def fillings(self):
        return self.find_element(*fillings)

    # Метод нажимает кнопку "Булки"
    def button_constructor_burgers_buns(self):
        self.construct_burger_buns().click()

    # Метод нажимает кнопку "Соусы"
    def button_constructor_burgers(self):
        self.constructor_burgers().click()

    # Метод нажимает кнопку "Начинки"
    def button_constructor_burgers_fillings(self):
        self.constructor_burgers_fillings().click()

    # Метод нажимает кнопку "Конструктор"
    def button_constructor_click(self):
        self.button_constructor_logo().click()
