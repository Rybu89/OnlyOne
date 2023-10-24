import allure
from elements.input_fields import InputFields

IF = InputFields()

@allure.description('Валидация полей ввода на странице.')
def test_validation_input_field(standard_preparation):

    IF.validation_field_name()
    IF.validation_field_email()
    IF.validation_field_telephone()
    IF.validation_field_company()
    IF.validation_field_tell_about_your_project()
