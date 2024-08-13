import pytest
from selenium import webdriver
from landing_page_scooter import LandingPageScooter
from testdata import ApplicationData


@pytest.fixture(scope='function')
def landing_page():
    driver = webdriver.Firefox()
    driver.get(ApplicationData.SCOOTER_URL)
    landing_page = LandingPageScooter(driver)

    yield landing_page

    driver.quit()
