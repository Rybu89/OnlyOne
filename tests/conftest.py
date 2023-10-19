import time
import pytest
from base.base_class import Base

base = Base()

# @pytest.fixture(scope="module")
# def from_module():
#
#     """ Очистка куков перед запуском тестов. Запрос на удаление скриншотов, после прогона. """
#
#     print('\nSTART')
#     base.browser.delete_all_cookies()
#
#     yield
#     # base.save_cookies('selected_brief_questionnaire_')
#     # base.deleting_all_screenshots()
#     time.sleep(3)
#     base.browser.quit()
#     print('\n FINISH')


@pytest.fixture()
def standard_preparation():

    """ Подготовка к прогону теста. """

    print('\n Running the test.')
    base.browser.get('https://only.digital/projects#brief')

    yield
    print('\n Completing the test.')


