from pages.register_page import RegisterPage


def test_register_page(browser):
    register_page = RegisterPage(browser)
    register_page.open()

    register_page.send_keys_register_button()
    register_page.button()

    register_page.time_authorization(browser)

