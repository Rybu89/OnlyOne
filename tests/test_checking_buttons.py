import allure
from elements.attach_buttons import AttachButtons
from elements.checkboxes import Checkboxes
from elements.radio_buttons import RadioButtons

Ab = AttachButtons()
Rb = RadioButtons()
Ch = Checkboxes()

@allure.description('Проверка всех кнопок на странице')
def test_checking_buttons(standard_preparation):

    Ab.checking_button_attach_file()
    Ab.checking_button_delete_attach_file()
    Ch.checking_status_change_checkboxes()
    Rb.checking_status_change_radiobutton()
