import os
from selenium.webdriver import ActionChains as Ac
from selenium.webdriver import Keys
from base.base_class import Base


class InputFields(Base):

    # Test data

    invalid_length_data_for_field = open(
        f'{os.getcwd()}\\tests_data\\invalid_length_data_for_field.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    invalid_data_for_field = open(f'{os.getcwd()}\\tests_data\\invalid_data_for_field.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    valid_data_for_field_name = open(f'{os.getcwd()}\\tests_data\\valid_data_for_field_name.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    valid_data_for_field_email = open(f'{os.getcwd()}\\tests_data\\valid_data_for_field_email.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    invalid_format_data_for_field_email = open(
        f'{os.getcwd()}\\tests_data\\invalid_format_data_for_field_email.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    valid_data_for_field_company = open(
        f'{os.getcwd()}\\tests_data\\valid_data_for_field_company.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    valid_data_for_field_telephone = open(
        f'{os.getcwd()}\\tests_data\\valid_data_for_field_telephone.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    invalid_format_for_field_telephone = open(
        f'{os.getcwd()}\\tests_data\\invalid_format_for_field_telephone.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    valid_data_for_field_tell_about_your_project = open(
        f'{os.getcwd()}\\tests_data\\valid_data_for_field_tell_about_your_project.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    # Locators

    locator_field_name = '//input[contains(@name, "name")]'
    locator_field_email = '//input[contains(@name, "email")]'
    locator_field_company = '//input[contains(@name, "company")]'
    locator_field_telephone = '//input[contains(@name, "phone")]'
    locator_field_tell_about_your_project = '//textarea[contains(@name, "description")]'
    locator_error_tell_about_your_project = '//div[contains(@class, "ktozux")]//p[contains(@class, "yfLgG")]'

    locator_error_message_invalid_format_for_all_fields = '//p[contains(@class, "yfLgG")]'
    locator_button_to_send = '//span[contains(@class, "dYqUsO")]'
    locator_title_page = '//span[contains(text(),"Сайт")]'
    locator_scroll_page = '//div[contains(@class, "crollbar-thumb")]'

    # Actions
    def select_and_clear_field(self, locator_field):
        """ Выбрать и очистить поле ввода. """

        Ac(self.browser).move_to_element(self.get_clickable_element(locator_field)).click()
        self.get_clickable_element(locator_field).send_keys(Keys.CONTROL + "a")
        self.get_clickable_element(locator_field).send_keys(Keys.DELETE)

    def validation_field_by_attribute(self, locator_field, data, attribute, value_attribute):
        """ Валидация полей вода, по возвращаемому атрибуту элементов.
                Проверки:
                    - реакция на ввод невалидных значений, вывод сообщения об ошибке 'Обязательное поле';
                    - реакция на ввод невалидных значений, вывод сообщения об ошибке 'Неверный формат';
                    - реакция на ввод невалидных значений, вывод сообщения об ошибке 'Превышено максимальное количество
                        символов';
                    - реакция на ввод валидных значений.
                Принимает:
                    locator_field - локатор поля/полей ввода (Str);
                    data - тестовые данные для валидации поля/полей (Str);
                    attribute - название атрибута элементов содержащий сообщение об ошибке ввода (Str);
                    value_attribute - ожидаемое сообщение об ошибке (Str).
        """

        if value_attribute == 'Обязательное поле':
            try:
                self.select_and_clear_field(locator_field)
                self.get_clickable_element(locator_field).send_keys(data[0])
                self.select_and_clear_field(locator_field)
                self.get_clickable_element(locator_field).send_keys(Keys.TAB)
                error = self.get_visibility_element(locator_field).get_attribute(attribute)
                assert error == value_attribute
                print(f"___Validation ОР={value_attribute}, ФР={error} __PASSED")
            except AssertionError:
                print(f"FAILED___ ОР={value_attribute}, ФР={error}")
            self.screenshot('validation_field_empty_')

        elif value_attribute == 'Неверный формат':
            index = 0
            for _ in data:
                try:
                    self.select_and_clear_field(locator_field)
                    self.get_clickable_element(locator_field).send_keys(data[index])
                    self.get_clickable_element(locator_field).send_keys(Keys.TAB)
                    error = self.get_visibility_element(locator_field).get_attribute(attribute)
                    assert error == value_attribute
                    print(f"___Validation ОР={value_attribute}, ФР={error} __PASSED")
                except AssertionError:
                    print(f"FAILED___ ОР={value_attribute}, ФР={error}")
                self.screenshot('validation_field_valid_')
                index = index + 1

        elif value_attribute == 'Превышено максимальное количество символов':
            index = 0
            for _ in data:
                try:
                    self.select_and_clear_field(locator_field)
                    self.get_clickable_element(locator_field).send_keys(data[index])
                    self.get_clickable_element(locator_field).send_keys(Keys.TAB)
                    error = self.get_visibility_element(locator_field).get_attribute(attribute)
                    assert error == value_attribute
                    print(f"___Validation ОР={value_attribute}, ФР={error} __PASSED")
                except AssertionError:
                    print(f"FAILED___ ОР={value_attribute}, ФР={error}")
                self.screenshot('validation_field_valid_')
                index = index + 1

        elif value_attribute is None:
            index = 0
            for _ in data:
                try:
                    self.select_and_clear_field(locator_field)
                    self.get_clickable_element(locator_field).send_keys(data[index])
                    self.get_clickable_element(locator_field).send_keys(Keys.TAB)
                    error = self.get_visibility_element(locator_field).get_attribute(attribute)
                    assert value_attribute is None and value_attribute == error
                    print(f"___Validation ОР={value_attribute}, ФР={error} __PASSED")
                except AssertionError:
                    print(f"FAILED___ ОР={value_attribute}, ФР={error}")
                self.screenshot('validation_field_valid_')
                index = index + 1

        else:
            print('FAILED___ Задана неизвестная валидация.')

    def validation_field_by_error_message(self, locator_field, data, locator_error_message, expected_result):
        """ Валидация полей вода, по возвращаемому тексту в тегах.
                Проверки:
                    - реакция на ввод невалидных значений, вывод сообщения об ошибке 'Неверный формат';
                    - реакция на ввод невалидных значений, вывод сообщения об ошибке 'Превышено максимальное количество
                        символов';
                    - реакция на ввод валидных значений.
                Принимает:
                    locator_field - локатор поля/полей ввода (Str);
                    data - тестовые данные для валидации поля/полей (Str);
                    locator_error_message - локатор тега содержащего сообщение об ошибке ввода (Str);
                    expected_result - ожидаемое сообщение об ошибке (Str).
        """

        if expected_result == 'Неверный формат':
            index = 0
            for _ in data:
                try:
                    self.select_and_clear_field(locator_field)
                    self.get_clickable_element(locator_field).send_keys(data[index])
                    self.get_clickable_element(locator_field).send_keys(Keys.TAB)
                    error_message = self.get_visibility_element(locator_error_message).text
                    assert error_message == expected_result
                    print(f"___Validation ОР={expected_result}, ФР={error_message} __PASSED")
                except AssertionError:
                    print(f"FAILED___ ОР={expected_result}, ФР={error_message}")
                self.screenshot('validation_field_valid_')
                index = index + 1

        elif expected_result == 'Превышено максимальное количество символов':
            index = 0
            for _ in data:
                try:
                    self.select_and_clear_field(locator_field)
                    self.get_clickable_element(locator_field).send_keys(data[index])
                    self.get_clickable_element(locator_field).send_keys(Keys.TAB)
                    error_message = self.get_visibility_element(locator_error_message).text
                    assert error_message == expected_result
                    print(f"___Validation ОР={expected_result}, ФР={error_message} __PASSED")
                except AssertionError:
                    print(f"FAILED___ ОР={expected_result}, ФР={error_message}")
                self.screenshot('validation_field_valid_')
                index = index + 1
        elif expected_result is None:
            index = 0
            for _ in data:
                try:
                    self.select_and_clear_field(locator_field)
                    self.get_clickable_element(locator_field).send_keys(data[index])
                    self.get_clickable_element(locator_field).send_keys(Keys.TAB)
                    error_message = self.check_exists_element_by_xpath(locator_error_message)
                    assert error_message == expected_result
                    print(f"___Validation ОР={expected_result}, ФР={error_message} __PASSED")
                except AssertionError:
                    print(f"FAILED___ ОР={expected_result}, ФР={error_message}")
                self.screenshot('validation_field_valid_')
                index = index + 1
        else:
            print('FAILED___ Задана неизвестная валидация.')

    # Methods

    def validation_field_name(self):

        self.validation_field_by_attribute(locator_field=self.locator_field_name,
                                           data=self.valid_data_for_field_name,
                                           attribute='error',
                                           value_attribute='Обязательное поле')

        self.validation_field_by_attribute(locator_field=self.locator_field_name,
                                           data=self.invalid_data_for_field,
                                           attribute='error',
                                           value_attribute='Неверный формат')

        self.validation_field_by_attribute(locator_field=self.locator_field_name,
                                           data=self.invalid_length_data_for_field,
                                           attribute='error',
                                           value_attribute='Превышено максимальное количество символов')

        self.validation_field_by_attribute(locator_field=self.locator_field_name,
                                           data=self.valid_data_for_field_name,
                                           attribute='error',
                                           value_attribute=None)

        print('___Validation field Name __PASSED')

    def validation_field_email(self):

        self.validation_field_by_attribute(locator_field=self.locator_field_email,
                                           data=self.invalid_format_data_for_field_email,
                                           attribute='error',
                                           value_attribute='Неверный формат')

        self.validation_field_by_attribute(locator_field=self.locator_field_email,
                                           data=self.invalid_length_data_for_field,
                                           attribute='error',
                                           value_attribute='Превышено максимальное количество символов')

        self.validation_field_by_attribute(locator_field=self.locator_field_email,
                                           data=self.valid_data_for_field_email,
                                           attribute='error',
                                           value_attribute='Обязательное поле')

        self.validation_field_by_attribute(locator_field=self.locator_field_email,
                                           data=self.valid_data_for_field_email,
                                           attribute='error',
                                           value_attribute=None)

        print('___Validation field Email __PASSED')

    def validation_field_telephone(self):

        self.validation_field_by_attribute(locator_field=self.locator_field_telephone,
                                           data=self.valid_data_for_field_telephone,
                                           attribute='error',
                                           value_attribute='Обязательное поле')

        self.validation_field_by_attribute(locator_field=self.locator_field_telephone,
                                           data=self.invalid_format_for_field_telephone,
                                           attribute='error',
                                           value_attribute='Неверный формат')

        self.validation_field_by_attribute(locator_field=self.locator_field_telephone,
                                           data=self.valid_data_for_field_telephone,
                                           attribute='error',
                                           value_attribute=None)

        print('___Validation field Telephone __PASSED')

    def validation_field_company(self):

        self.validation_field_by_attribute(locator_field=self.locator_field_company,
                                           data=self.invalid_data_for_field,
                                           attribute='error',
                                           value_attribute='Неверный формат')

        self.validation_field_by_attribute(locator_field=self.locator_field_company,
                                           data=self.invalid_length_data_for_field,
                                           attribute='error',
                                           value_attribute='Превышено максимальное количество символов')

        self.validation_field_by_attribute(locator_field=self.locator_field_company,
                                           data=self.valid_data_for_field_company,
                                           attribute='error',
                                           value_attribute=None)

        print('___Validation field Company __PASSED')

    def validation_field_tell_about_your_project(self):
        self.validation_field_by_error_message(locator_field=self.locator_field_tell_about_your_project,
                                               data=self.invalid_data_for_field,
                                               locator_error_message=self.locator_error_tell_about_your_project,
                                               expected_result='Неверный формат')

        self.validation_field_by_error_message(locator_field=self.locator_field_tell_about_your_project,
                                               data=self.invalid_length_data_for_field,
                                               locator_error_message=self.locator_error_tell_about_your_project,
                                               expected_result='Превышено максимальное количество символов')

        self.validation_field_by_error_message(locator_field=self.locator_field_tell_about_your_project,
                                               data=self.valid_data_for_field_tell_about_your_project,
                                               locator_error_message=self.locator_error_tell_about_your_project,
                                               expected_result=None)

        print('___Validation field Tell about your project __PASSED')
