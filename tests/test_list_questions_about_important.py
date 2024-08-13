import pytest
from utils import Utils
from testdata import Data


class TestListQuestionsAboutImportant:
    @pytest.mark.parametrize('index, text_answer', Utils.enumerated(Data.answers))
    def test_answer(self, landing_page, index, text_answer):
        landing_page.scroll_question_about_important()
        landing_page.wait_question_button(index)
        landing_page.click_question_button(index)
        landing_page.wait_answer(index)
        landing_page.check_answer_is_displayed(index)
        landing_page.check_answer_text(index, text_answer)
