from selenium.webdriver.common.by import By


class LocatorsLandingPageScooter:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    YANDEX_LOGO = (By.XPATH, './/*[@href = "//yandex.ru"]')
    DZEN_LOGO = (By.XPATH, './/a[@aria-label = "Логотип Бренда"]')
    SCOOTER_PNG = (By.XPATH, './/img[@alt = "Scooter blueprint"]')
    HEADER_ORDER_BUTTON = (By.XPATH, './/div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')
    PRIMARY_ORDER_BUTTON = (By.XPATH, './/div[@class = "Home_ThirdPart__LSTEE"]//button[text() = "Заказать"]')

    @staticmethod
    def get_question_locator(index):
        return By.ID, f'accordion__heading-{index}'

    @staticmethod
    def get_answer_locator(index):
        return By.ID, f'accordion__panel-{index}'
