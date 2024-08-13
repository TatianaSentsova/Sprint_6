from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from landing_page_locators import LocatorsLandingPageScooter


class LandingPageScooter:
    def __init__(self, driver):
        self.driver = driver

    def scroll_question_about_important(self):
        list_about_important = self.driver.find_element(*LocatorsLandingPageScooter.list_about_important)
        self.driver.execute_script("arguments[0].scrollIntoView();", list_about_important)

    def wait_question_button(self, index):
        locator = LocatorsLandingPageScooter.get_question_locator(index)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    def click_question_button(self, index):
        locator = LocatorsLandingPageScooter.get_question_locator(index)
        self.driver.find_element(*locator).click()

    def wait_answer(self, index):
        locator = LocatorsLandingPageScooter.get_answer_locator(index)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    def check_answer_is_displayed(self, index):
        locator = LocatorsLandingPageScooter.get_answer_locator(index)
        answer = self.driver.find_element(*locator)
        assert answer.is_displayed()

    def get_answer(self, index):
        locator = LocatorsLandingPageScooter.get_answer_locator(index)
        return self.driver.find_element(*locator).text

    def check_answer_text(self, index, expected_value):
        actually_value = self.get_answer(index)
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}"'
