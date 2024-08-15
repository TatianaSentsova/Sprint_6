import random
from order_page_locators import LocatorsOrderPageScooter
from testdata import DataOrder
from utils import Utils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderPageScooter:
    @allure.step('Подгружаем драйвер в конструктор')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем когда загрузится страница с формой заказа')
    def wait_order_page_loading(self):
        locator = LocatorsOrderPageScooter.HEADER_ORDER_FORM_ABOUT_USER
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))

    @allure.step('Находим заголовок формы заказа')
    def get_order_form(self):
        locator = LocatorsOrderPageScooter.HEADER_ORDER_FORM_ABOUT_USER
        return self.driver.find_element(*locator)

    @allure.step('Кликаем по логотипу Самоката')
    def click_click_on_scooter_logo(self):
        locator = LocatorsOrderPageScooter.SCOOTER_LOGO
        self.driver.find_element(*locator).click()

    @allure.step('Вводим имя')
    def set_first_name(self, first_name):
        locator = LocatorsOrderPageScooter.FIRST_NAME_FIELD
        self.driver.find_element(*locator).send_keys(first_name)

    @allure.step('Вводим фамилию')
    def set_last_name(self, last_name):
        locator = LocatorsOrderPageScooter.LAST_NAME_FIELD
        self.driver.find_element(*locator).send_keys(last_name)

    @allure.step('Вводим адрес')
    def set_address(self, address):
        locator = LocatorsOrderPageScooter.ADDRESS_FIELD
        self.driver.find_element(*locator).send_keys(address)

    @allure.step('Выбираем станцию метро')
    def select_station_subway(self):
        locator = LocatorsOrderPageScooter.STATION_SUBWAY_FIELD
        self.driver.find_element(*locator).click()
        station_subway = random.choice(DataOrder.STATION_SUBWAY)
        locator_list = LocatorsOrderPageScooter.choose_station_subway(station_subway)
        self.driver.find_element(*locator_list).click()

    @allure.step('Вводим номер телефона')
    def set_phone_number(self):
        phone_number = Utils.generation_phone_number()
        locator = LocatorsOrderPageScooter.PHONE_NUMBER_FIELD
        self.driver.find_element(*locator).send_keys(phone_number)

    @allure.step('Кликаем по кнопке "Далее"')
    def click_order_next_button(self):
        locator = LocatorsOrderPageScooter.ORDER_NEXT_BUTTON
        self.driver.find_element(*locator).click()

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
        locator = LocatorsOrderPageScooter.DATE_FIELD
        self.driver.find_element(*locator).send_keys(date)

    @allure.step('Выбираем срок аренды')
    def choose_rental_period(self):
        locator = LocatorsOrderPageScooter.RENTAL_PERIOD_FIELD
        self.driver.find_element(*locator).click()
        period = random.choice(DataOrder.PERIOD_RENTAL)
        locator_period = LocatorsOrderPageScooter.choose_rental_period(period)
        self.driver.find_element(*locator_period).click()

    @allure.step('Выбираем цвет самоката')
    def choose_color_scooter(self):
        color = random.choice(DataOrder.COLOR)
        locator = LocatorsOrderPageScooter.choose_color(color)
        self.driver.find_element(*locator).click()

    @allure.step('Вводим информацию о заказе')
    def set_form_about_rental(self, date):
        self.set_date(date)
        self.choose_rental_period()
        self.choose_color_scooter()

    @allure.step('Нажимаем кнопку "Заказать" и  подтверждаем заказ')
    def make_order(self):
        self.driver.find_element(*LocatorsOrderPageScooter.ORDER_BUTTON).click()
        self.driver.find_element(*LocatorsOrderPageScooter.CONFIRM_BUTTON).click()

    @allure.step('Находим сообщение об оформлении заказа')
    def get_order_success_message(self):
        locator = LocatorsOrderPageScooter.ORDER_SUCCESS_MESSAGE
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)
