import random
from order_page_locators import LocatorsOrderPageScooter
from testdata import Data
from utils import Utils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPageScooter:
    def __init__(self, driver):
        self.driver = driver

    def wait_order_page_loading(self):
        locator = LocatorsOrderPageScooter.HEADER_ORDER_FORM_ABOUT_USER
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))

    def get_order_form(self):
        locator = LocatorsOrderPageScooter.HEADER_ORDER_FORM_ABOUT_USER
        return self.driver.find_element(*locator)

    def click_click_on_scooter_logo(self):
        locator = LocatorsOrderPageScooter.SCOOTER_LOGO
        self.driver.find_element(*locator).click()

    def set_first_name(self, first_name):
        locator = LocatorsOrderPageScooter.FIRST_NAME_FIELD
        self.driver.find_element(*locator).send_keys(first_name)

    def set_last_name(self, last_name):
        locator = LocatorsOrderPageScooter.LAST_NAME_FIELD
        self.driver.find_element(*locator).send_keys(last_name)

    def set_address(self, address):
        locator = LocatorsOrderPageScooter.ADDRESS_FIELD
        self.driver.find_element(*locator).send_keys(address)

    def select_station_subway(self):
        locator = LocatorsOrderPageScooter.STATION_SUBWAY_FIELD
        self.driver.find_element(*locator).click()
        station_subway = random.choice(Data.STATION_SUBWAY)
        locator_list = LocatorsOrderPageScooter.choose_station_subway(station_subway)
        self.driver.find_element(*locator_list).click()

    def set_phone_number(self):
        phone_number = Utils.generation_phone_number()
        locator = LocatorsOrderPageScooter.PHONE_NUMBER_FIELD
        self.driver.find_element(*locator).send_keys(phone_number)

    def click_order_next_button(self):
        locator = LocatorsOrderPageScooter.ORDER_NEXT_BUTTON
        self.driver.find_element(*locator).click()

    def set_form_about_user(self, first_name, last_name, address):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.select_station_subway()
        self.set_phone_number()
        self.click_order_next_button()

    def set_date(self, date):
        locator = LocatorsOrderPageScooter.DATE_FIELD
        self.driver.find_element(*locator).send_keys(date)

    def set_rental_period(self):
        locator = LocatorsOrderPageScooter.RENTAL_PERIOD_FIELD
        self.driver.find_element(*locator).click()
        period = random.choice(Data.PERIOD_RENTAL)
        locator_period = LocatorsOrderPageScooter.choose_rental_period(period)
        self.driver.find_element(*locator_period).click()

    def choose_color_scooter(self):
        color = random.choice(Data.COLOR)
        locator = LocatorsOrderPageScooter.choose_color(color)
        self.driver.find_element(*locator).click()

    def set_form_about_rental(self, date):
        self.set_date(date)
        self.set_rental_period()
        self.choose_color_scooter()

    def make_order(self):
        self.driver.find_element(*LocatorsOrderPageScooter.ORDER_BUTTON).click()
        self.driver.find_element(*LocatorsOrderPageScooter.YES_BUTTON).click()

    def get_order_success_message(self):
        locator = LocatorsOrderPageScooter.ORDER_SUCCESS_MESSAGE
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)
