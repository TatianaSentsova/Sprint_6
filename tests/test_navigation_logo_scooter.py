import allure
from testdata import ApplicationData


class TestNavigationLogoScooter:
    @allure.title('Проверяем открытие в новом окне домашней страницы Яндекса, при нажатии на лого Яндекса')
    def test_click_on_yandex_logo_and_open_dzen(self, driver, landing_page):
        landing_page.click_cookie_button()
        landing_page.click_yandex_logo()
        landing_page.switch_to_dzen_window_and_loading_page()
        assert landing_page.get_current_url() == ApplicationData.DZEN_URL

    @allure.title('Проверяем возвращение на главную страницу Самоката, при нажатии на лого Самоката')
    def test_click_on_scooter_logo_and_open_home_page(self, landing_page, order_page):
        landing_page.click_cookie_button()
        landing_page.click_header_order_button()
        order_page.wait_order_page_loading()
        order_page.click_on_scooter_logo()
        assert landing_page.get_current_url() == ApplicationData.SCOOTER_URL
