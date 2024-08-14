from testdata import ApplicationData


class TestNavigationLogoScooter:
    def test_click_on_yandex_logo_and_open_dzen(self, driver, landing_page):
        landing_page.click_cookie_button()
        landing_page.click_yandex_logo()
        landing_page.switch_to_dzen_window_and_loading_page()
        assert driver.current_url == ApplicationData.DZEN_URL

    def test_click_on_scooter_logo_and_open_home_page(self, landing_page, order_page):
        landing_page.click_cookie_button()
        landing_page.click_header_order_button()
        order_page.wait_order_page_loading()
        order_page.click_click_on_scooter_logo()
        element = landing_page.get_scooter_png()
        assert element.is_displayed
