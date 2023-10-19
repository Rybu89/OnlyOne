import pytest
import allure
from elements.titles_and_names import TitlesAndNames


TaN = TitlesAndNames()

@allure.description('Checking for all elements on the page')
def test_checking_for_elements_on_the_page(standard_preparation):

    TaN.check_title_brief_questionnaire_page()
    TaN.check_existing_sections()
    # TaN.check_existing_radio_buttons()
    # TaN.check_existing_messages()
    # TaN.check_existing_input_fields()
    # TaN.check_existing_buttons()
