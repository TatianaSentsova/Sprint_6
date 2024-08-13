from selenium.webdriver.common.by import By


class LocatorsLandingPageScooter:
    list_about_important = (By.XPATH, './/div[text() = "Вопросы о важном"]')

    @staticmethod
    def get_question_locator(index):
        return By.ID, f'accordion__heading-{index}'

    @staticmethod
    def get_answer_locator(index):
        return By.ID, f'accordion__panel-{index}'
