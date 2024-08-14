import pytest


class TestOrderScooter:
    def test_open_order_by_header_button(self, landing_page, order_page):
        landing_page.click_cookie_button()
        landing_page.click_header_order_button()
        order_page.wait_order_page_loading()
        order_page.check_order_form()

    def test_open_order_by_primary_button(self, landing_page, order_page):
        landing_page.click_cookie_button()
        landing_page.scroll_primary_order_button()
        landing_page.click_primary_order_button()
        order_page.wait_order_page_loading()
        order_page.check_order_form()

    @pytest.mark.parametrize('first_name, last_name, address, date', [['Таня', 'Сенцова', 'Попова 5', '20.08.2014'],
                                                                      ['Янат', 'Авоцнес', 'Иванова 5', '25.08.2014']])
    def test_order_scooter(self, landing_page, order_page, first_name, last_name, address, date):
        landing_page.click_cookie_button()
        landing_page.click_header_order_button()
        order_page.wait_order_page_loading()
        order_page.set_form_about_user(first_name, last_name, address)
        order_page.set_form_about_rental(date)
        order_page.make_order()
        order_page.check_order_success_message()
