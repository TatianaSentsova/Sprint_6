from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from landing_page_locators import LandingPageLocators
import allure


class LandingPageScooter:
    @allure.step('Подгружаем драйвер в конструктор')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Соглашаемся на использование куки')
    def click_cookie_button(self):
        locator = LandingPageLocators.COOKIE_BUTTON
        self.driver.find_element(*locator).click()

    @allure.step('Кликаем по логотипу Яндекса')
    def click_yandex_logo(self):
        locator = LandingPageLocators.YANDEX_LOGO
        self.driver.find_element(*locator).click()

    @allure.step('Находим картинку самоката на лендинге')
    def get_scooter_png(self):
        locator = LandingPageLocators.SCOOTER_PNG
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Скроллим страницу до нужного вопроса')
    def scroll_question(self, index):
        element = self.driver.find_element(*LandingPageLocators.get_question_locator(index))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидаем, когда вопрос станет кликабельным, и кликаем по нему')
    def click_question_button(self, index):
        locator = LandingPageLocators.get_question_locator(index)
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ожидаем появления ответа')
    def wait_answer(self, index):
        locator = LandingPageLocators.get_answer_locator(index)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    @allure.step('Проверяем, что ответ отобразился на странице')
    def check_answer(self, index):
        locator = LandingPageLocators.get_answer_locator(index)
        assert self.driver.find_element(*locator).is_displayed

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, index):
        locator = LandingPageLocators.get_answer_locator(index)
        return self.driver.find_element(*locator).text

    @allure.step('Кликаем по кнопке заказать ')
    def click_header_order_button(self):
        locator = LandingPageLocators.HEADER_ORDER_BUTTON
        self.driver.find_element(*locator).click()

    @allure.step('Скроллим до кнопки "Заказать" в основной части лендинга')
    def scroll_primary_order_button(self,):
        element = self.driver.find_element(*LandingPageLocators.PRIMARY_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидаем, когда кнопка "Заказать" появится на странице и кликаем по ней')
    def click_primary_order_button(self):
        locator = LandingPageLocators.PRIMARY_ORDER_BUTTON
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Переходим в новое окно браузера и ждем прогрузки страницы')
    def switch_to_dzen_window_and_loading_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        locator = LandingPageLocators.DZEN_LOGO
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
