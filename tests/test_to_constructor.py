from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.constructor_page import ConstructorPage
from tests.urls import URL_SITE


class TestBurgerPersonalAcount:
    def test_personal_account_to_constructor_page(self, browser):
        # создал объект класса
        constructor = ConstructorPage(browser)
        # Открываем страницу
        constructor.open()

        # Нажимаем кнопку "Личный Кабинет"
        constructor.button_constructor_click()

        # Явное ожидание загрузки страницы
        wait = WebDriverWait(browser, 10)
        wait.until(EC.url_to_be(URL_SITE))

        assert browser.current_url == URL_SITE

    def test_navigation_to_sauces_section(self, browser):
        # создал объект класса
        constructor = ConstructorPage(browser)
        # Открываем страницу
        constructor.open_burger()

        # Нажимаем "Соусы"
        constructor.button_constructor_burgers()

        assert constructor.get_text_sauces() == 'Соусы'

    def test_navigation_to_fillings_section(self, browser):
        # создал объект класса
        constructor = ConstructorPage(browser)
        # Открываем страницу
        constructor.open_burger()

        # Нажимаем "Начинки"
        constructor.button_constructor_burgers_fillings()

        assert constructor.get_text_fillings() == 'Начинки'

    def test_navigation_to_buns_section(self, browser):
        # создал объект класса
        constructor = ConstructorPage(browser)
        # Открываем страницу
        constructor.open_burger()

        # Нажимаем "Соусы", чтобы потом переключиться на "Булки"
        constructor.button_constructor_burgers()

        # Нажимаем на "Булки"
        constructor.button_constructor_burgers_buns()

        assert constructor.get_text_buns() == 'Булки'
