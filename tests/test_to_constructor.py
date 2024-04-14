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

        # Получаем новый класс элемента "Соусы"
        new_class = constructor.sauces().get_attribute("class")

        # Сравниваем полученный элемент с ожидаемым
        assert 'tab_tab_type_current__2BEPc' in new_class

    def test_navigation_to_fillings_section(self, browser):
        # создал объект класса
        constructor = ConstructorPage(browser)
        # Открываем страницу
        constructor.open_burger()

        # Нажимаем "Начинки"
        constructor.button_constructor_burgers_fillings()

        # Получаем новый класс элемента "Начинки"
        new_class = constructor.fillings().get_attribute("class")

        # Сравниваем полученный элемент с ожидаемым
        assert 'tab_tab_type_current__2BEPc' in new_class

    def test_navigation_to_buns_section(self, browser):
        # создал объект класса
        constructor = ConstructorPage(browser)
        # Открываем страницу
        constructor.open_burger()

        # Нажимаем "Соусы", чтобы потом переключиться на "Булки"
        constructor.button_constructor_burgers()

        # Нажимаем на "Булки"
        constructor.button_constructor_burgers_buns()

        # Получаем новый класс элемента "Булки"
        new_class = constructor.buns().get_attribute("class")

        # Сравниваем полученный элемент с ожидаемым
        assert 'tab_tab_type_current__2BEPc' in new_class
