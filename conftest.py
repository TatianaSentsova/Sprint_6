import pytest
from selenium import webdriver
from landing_page_scooter import LandingPageScooter
from order_page_skooter import OrderPageScooter
from testdata import ApplicationData


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(ApplicationData.SCOOTER_URL)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def landing_page(driver):
    landing_page = LandingPageScooter(driver)
    return landing_page


@pytest.fixture(scope='function')
def order_page(driver):
    order_page = OrderPageScooter(driver)
    return order_page
