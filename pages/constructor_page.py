from selenium.webdriver.common.by import By
from pages.base_page import BasePage

button_constructor_selector = (By.XPATH, "//p[contains(text(),'Конструктор')]")
logo_constructor_selector = (By.XPATH, "//a[@href='/']")
constructor_burger_selector_1 = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']/div/div[2]")
constructor_burger_selector_2 = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']/div/div[1]")
constructor_burger_selector_3 = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']/div/div[3]")
constructor_burger_selector_4 = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']/div/div[2]/span")
constructor_burger_selector_5 = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']/div/div[3]/span")
constructor_burger_selector_6 = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']/div/div[1]/span")


class ConstructorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_logo_stellar_burgers(self):
        self.browser.get('https://stellarburgers.nomoreparties.site/login')

    def open_constructor(self):
        self.browser.get('https://stellarburgers.nomoreparties.site/login')

    def open_burger(self):
        self.browser.get('https://stellarburgers.nomoreparties.site/')

    # Метод возвращает локатор логотипа "stellar_burgers"
    def button_constructor_logo(self):
        return self.find_element(*logo_constructor_selector)

    # Метод возвращает локатор "Булки"
    def construct_burger_buns(self):
        return self.find_element(*constructor_burger_selector_2)

    # Метод возвращает локатор "Соусы"
    def constructor_burgers(self):
        return self.find_element(*constructor_burger_selector_1)

    # Метод возвращает локатор "Начинки"
    def constructor_burgers_fillings(self):
        return self.find_element(*constructor_burger_selector_3)

    # Метод нажимает кнопку "Булки"
    def button_constructor_burgers_buns(self):
        self.construct_burger_buns().click()

    # Метод нажимает кнопку "Соусы"
    def button_constructor_burgers(self):
        self.constructor_burgers().click()

    # Метод нажимает кнопку "Начинки"
    def button_constructor_burgers_fillings(self):
        self.constructor_burgers_fillings().click()

    # Метод возвращает локатор текста "Булки"
    def get_text_buns(self):
        element = self.find_element(*constructor_burger_selector_6)
        return element.text  # Возвращаем текст элемента

    # Метод возвращает локатор текста "Соусы"
    def get_text_sauces(self):
        element = self.find_element(*constructor_burger_selector_4)
        return element.text  # Возвращаем текст элемента

    # Метод возвращает локатор текста "Начинки"
    def get_text_fillings(self):
        element = self.find_element(*constructor_burger_selector_5)
        return element.text  # Возвращаем текст элемента

    # Метод нажимает кнопку "Конструктор"
    def button_constructor_click(self):
        self.button_constructor_logo().click()
