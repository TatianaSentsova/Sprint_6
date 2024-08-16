import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    @allure.step('Подгружаем драйвер в конструктор')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загружаем страницу')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Получаем элемент')
    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    @allure.step('Ожидаем, что элемент появился на странице и его видно')
    def find_and_wait_element_until_visible(self, locator):
        WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(locator))
        return self.find_element(locator)

    @allure.step('Ожидаем, что элемент на странице кликабелен')
    def find_and_wait_element_until_clickable(self, locator):
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(locator))
        return self.find_element(locator)

    @allure.step('Скроллим до элмента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step('Вводим текст в элемент')
    def set_text_to_element(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step('Получаем текст элемента')
    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step('Переходим в новое окно')
    def switch_to_new_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получаем url активной страницы')
    def get_current_url(self):
        return self.driver.current_url
