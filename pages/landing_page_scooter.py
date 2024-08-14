from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from landing_page_locators import LocatorsLandingPageScooter


class LandingPageScooter:
    def __init__(self, driver):
        self.driver = driver

    def click_cookie_button(self):
        locator = LocatorsLandingPageScooter.COOKIE_BUTTON
        self.driver.find_element(*locator).click()

    def click_yandex_logo(self):
        locator = LocatorsLandingPageScooter.YANDEX_LOGO
        self.driver.find_element(*locator).click()

    def check_scooter_png(self):
        locator = LocatorsLandingPageScooter.SCOOTER_PNG
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        assert self.driver.find_element(*locator).is_displayed

    def scroll_question(self, index):
        element = self.driver.find_element(*LocatorsLandingPageScooter.get_question_locator(index))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_question_button(self, index):
        locator = LocatorsLandingPageScooter.get_question_locator(index)
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(locator))

    def click_question_button(self, index):
        locator = LocatorsLandingPageScooter.get_question_locator(index)
        self.driver.find_element(*locator).click()

    def wait_answer(self, index):
        locator = LocatorsLandingPageScooter.get_answer_locator(index)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    def check_answer(self, index):
        locator = LocatorsLandingPageScooter.get_answer_locator(index)
        assert self.driver.find_element(*locator).is_displayed

    def get_answer_text(self, index):
        locator = LocatorsLandingPageScooter.get_answer_locator(index)
        return self.driver.find_element(*locator).text

    def click_header_order_button(self):
        locator = LocatorsLandingPageScooter.HEADER_ORDER_BUTTON
        self.driver.find_element(*locator).click()

    def scroll_primary_order_button(self,):
        element = self.driver.find_element(*LocatorsLandingPageScooter.PRIMARY_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_primary_order_button(self, index):
        locator = LocatorsLandingPageScooter.PRIMARY_ORDER_BUTTON
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def click_primary_order_button(self):
        locator = LocatorsLandingPageScooter.PRIMARY_ORDER_BUTTON
        self.driver.find_element(*locator).click()

    def switch_to_dzen_window_and_loading_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        locator = LocatorsLandingPageScooter.DZEN_LOGO
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
