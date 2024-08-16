import random
import allure
from locators.order_page_locators import LocatorsOrderPageScooter
from testdata import DataOrder
from utils import Utils
from pages.base_page import BasePage


class OrderPageScooter(BasePage):
    @allure.step('Ожидаем когда загрузится страница с формой заказа')
    def wait_order_page_loading(self):
        self.find_and_wait_element_until_visible(LocatorsOrderPageScooter.HEADER_ORDER_FORM_ABOUT_USER)

    @allure.step('Получаем текст заголовка формы заказа')
    def get_header_order_form_text(self):
        return self.get_element_text(LocatorsOrderPageScooter.HEADER_ORDER_FORM_ABOUT_USER)

    @allure.step('Кликаем по логотипу Самоката')
    def click_on_scooter_logo(self):
        self.click_element(LocatorsOrderPageScooter.SCOOTER_LOGO)

    @allure.step('Вводим имя')
    def set_first_name(self, first_name):
        self.set_text_to_element(LocatorsOrderPageScooter.FIRST_NAME_FIELD, first_name)

    @allure.step('Вводим фамилию')
    def set_last_name(self, last_name):
        self.set_text_to_element(LocatorsOrderPageScooter.LAST_NAME_FIELD, last_name)

    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.set_text_to_element(LocatorsOrderPageScooter.ADDRESS_FIELD, address)

    @allure.step('Выбираем станцию метро')
    def select_station_subway(self):
        self.click_element(LocatorsOrderPageScooter.STATION_SUBWAY_FIELD)
        station_subway = random.choice(DataOrder.STATION_SUBWAY)
        self.click_element(LocatorsOrderPageScooter.choose_station_subway(station_subway))

    @allure.step('Вводим номер телефона')
    def set_phone_number(self):
        phone_number = Utils.generation_phone_number()
        self.set_text_to_element(LocatorsOrderPageScooter.PHONE_NUMBER_FIELD, phone_number)

    @allure.step('Кликаем по кнопке "Далее"')
    def click_order_next_button(self):
        self.click_element(LocatorsOrderPageScooter.ORDER_NEXT_BUTTON)

    @allure.step('Вводим персональные данные для заказа')
    def set_form_about_user(self, first_name, last_name, address):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.select_station_subway()
        self.set_phone_number()
        self.click_order_next_button()

    @allure.step('Вводим дату')
    def set_date(self, date):
        self.set_text_to_element(LocatorsOrderPageScooter.DATE_FIELD, date)

    @allure.step('Выбираем срок аренды')
    def choose_rental_period(self):
        self.click_element(LocatorsOrderPageScooter.RENTAL_PERIOD_FIELD)
        period = random.choice(DataOrder.PERIOD_RENTAL)
        self.click_element(LocatorsOrderPageScooter.choose_rental_period(period))

    @allure.step('Выбираем цвет самоката')
    def choose_color_scooter(self):
        color = random.choice(DataOrder.COLOR)
        self.click_element(LocatorsOrderPageScooter.choose_color(color))

    @allure.step('Вводим информацию о заказе')
    def set_form_about_rental(self, date):
        self.set_date(date)
        self.choose_rental_period()
        self.choose_color_scooter()

    @allure.step('Нажимаем кнопку "Заказать" и  подтверждаем заказ')
    def make_order(self):
        self.click_element(LocatorsOrderPageScooter.ORDER_BUTTON)
        self.click_element(LocatorsOrderPageScooter.CONFIRM_BUTTON)

    @allure.step('Получаем текст сообщения об оформлении заказа')
    def get_order_success_message_text(self):
        self.find_and_wait_element_until_clickable(LocatorsOrderPageScooter.ORDER_SUCCESS_MESSAGE)
        return self.get_element_text(LocatorsOrderPageScooter.ORDER_SUCCESS_MESSAGE)
