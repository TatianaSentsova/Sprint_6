from locators.landing_page_locators import LandingPageLocators
from pages.base_page import BasePage
import allure


class LandingPageScooter(BasePage):
    @allure.step('Соглашаемся на использование куки')
    def click_cookie_button(self):
        self.click_element(LandingPageLocators.COOKIE_BUTTON)

    @allure.step('Кликаем по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click_element(LandingPageLocators.YANDEX_LOGO)

    @allure.step('Скроллим страницу до нужного вопроса')
    def scroll_question(self, index):
        self.scroll_to_element(LandingPageLocators.get_question_locator(index))

    @allure.step('Ожидаем, когда вопрос станет кликабельным, и кликаем по нему')
    def click_question_button(self, index):
        self.find_and_wait_element_until_clickable(LandingPageLocators.get_question_locator(index))
        self.click_element(LandingPageLocators.get_question_locator(index))

    @allure.step('Ожидаем появления ответа')
    def wait_answer(self, index):
        self.find_and_wait_element_until_visible(LandingPageLocators.get_answer_locator(index))

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, index):
        return self.get_element_text(LandingPageLocators.get_answer_locator(index))

    @allure.step('Кликаем по кнопке заказать ')
    def click_header_order_button(self):
        self.click_element(LandingPageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Скроллим до кнопки "Заказать" в основной части лендинга')
    def scroll_primary_order_button(self,):
        self.find_and_wait_element_until_clickable(LandingPageLocators.PRIMARY_ORDER_BUTTON)
        self.scroll_to_element(LandingPageLocators.PRIMARY_ORDER_BUTTON)

    @allure.step('Ожидаем, когда кнопка "Заказать" появится на странице и кликаем по ней')
    def click_primary_order_button(self):
        self.find_and_wait_element_until_visible(LandingPageLocators.PRIMARY_ORDER_BUTTON)
        self.click_element(LandingPageLocators.PRIMARY_ORDER_BUTTON)

    @allure.step('Переходим в новое окно браузера и ждем прогрузки страницы')
    def switch_to_dzen_window_and_loading_page(self):
        self.switch_to_new_page()
        self.find_and_wait_element_until_visible(LandingPageLocators.DZEN_LOGO)
