from selenium.webdriver.common.by import By


class LocatorsLandingPageScooter:
    list_about_important = (By.XPATH, './/div[text() = "Вопросы о важном"]')
    painting_scooter = (By.XPATH, './/img[contains(@src, "blueprint.png")]')
    cookie_button = (By.ID, "rcc-confirm-button")

    @staticmethod
    def get_question_locator(index):
        return By.ID, f'accordion__heading-{index}'

    @staticmethod
    def get_answer_locator(index):
        return By.ID, f'accordion__panel-{index}'

    header_order_button = (By.XPATH, './/div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')
    primary_order_button = (By.XPATH, './/div[@class = "Home_ThirdPart__LSTEE"]//button[text() = "Заказать"]')
