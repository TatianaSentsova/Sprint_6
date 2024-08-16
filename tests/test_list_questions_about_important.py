import pytest
import allure
from utils import Utils
from testdata import Answers


class TestListQuestionsAboutImportant:
    @allure.title('Тестируем вопрос-ответ')
    @allure.description('Проверяем, что для каждого вопроса открывается соотвествующий ответ')
    @pytest.mark.parametrize('index, text_answer', Utils.enumerated(Answers.ANSWER))
    def test_answer(self, landing_page, index, text_answer):
        landing_page.click_cookie_button()
        landing_page.scroll_question(index)
        landing_page.click_question_button(index)
        landing_page.wait_answer(index)
        actually_value = landing_page.get_answer_text(index)
        assert actually_value == text_answer, f'Ожидалось значение: "{text_answer}"'
