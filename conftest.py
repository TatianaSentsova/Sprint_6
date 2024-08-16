import pytest
import allure
from selenium import webdriver
from testdata import ApplicationData
from pages.landing_page_scooter import LandingPageScooter
from pages.order_page_scooter import OrderPageScooter


@allure.step('Инициализируем драйвер')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def landing_page(driver):
    landing_page = LandingPageScooter(driver)
    landing_page.get_url(ApplicationData.SCOOTER_URL)
    return landing_page


@pytest.fixture
def order_page(driver):
    order_page = OrderPageScooter(driver)
    return order_page
