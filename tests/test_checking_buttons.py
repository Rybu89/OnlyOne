from elements.attach_buttons import AttachButtons
import allure

Ab = AttachButtons()
@allure.description('Checking the buttons for attaching files to pages')
def test_checking_button_attach_file(standard_preparation):
    """ Прикрепление файла. """

    Ab.checking_button_attach_file()

def test_checking_deleted_attach_file(standard_preparation):
    """ Удаление прикрепленного файла. """

    Ab.checking_delete_attach_file()

