from selenium.webdriver.common.by import By


class LandingPageLocators:
    # Кнопка "Принять куки"
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    # Логотип Яндекса
    YANDEX_LOGO = (By.XPATH, './/*[@href = "//yandex.ru"]')
    # Картинка в Логотипе Дзена
    DZEN_LOGO = (By.XPATH, './/a[@aria-label = "Логотип Бренда"]')
    # Картинка самоката на лендинге
    SCOOTER_PNG = (By.XPATH, './/img[@alt = "Scooter blueprint"]')
    # Кнопка "Заказать" в шапке лендинга
    HEADER_ORDER_BUTTON = (By.XPATH, './/div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')
    # Кнопка "Заказать" в основной часте лендинга
    PRIMARY_ORDER_BUTTON = (By.XPATH, './/div[@class = "Home_ThirdPart__LSTEE"]//button[text() = "Заказать"]')

    # Метод, возвращающий локаторы вопросов в разделе "Вопросы о важном"
    @staticmethod
    def get_question_locator(index):
        return By.ID, f'accordion__heading-{index}'

    # Метод, возвращающий локаторы ответов в разделе "Вопросы о важном"
    @staticmethod
    def get_answer_locator(index):
        return By.ID, f'accordion__panel-{index}'
