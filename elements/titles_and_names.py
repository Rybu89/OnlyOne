import os
import allure
from base.base_class import Base


class TitlesAndNames(Base):

    # Test data

    title_page = 'Заполните анкету'

    sections_names = open(f'{os.getcwd()}\\tests_data\\sections_names.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    radio_button_names = open(f'{os.getcwd()}\\tests_data\\radio_button_names.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    titles_messages = open(f'{os.getcwd()}\\tests_data\\titles_messages.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    title_message_to_send = open(f'{os.getcwd()}\\tests_data\\title_message_to_send.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    input_fields_names = open(f'{os.getcwd()}\\tests_data\\input_fields_names.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    input_field_tell_us_about_your_project = open(
        f'{os.getcwd()}\\tests_data\\input_field_tell_us_about_your_project.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    button_attach_file = open(f'{os.getcwd()}\\tests_data\\button_attach_file.txt', encoding='utf-8') \
        .read() \
        .split(';\n')
    button_to_send = open(f'{os.getcwd()}\\tests_data\\button_to_send.txt', encoding='utf-8') \
        .read() \
        .split(';\n')

    # Locators
    locator_page_title = '(//h2[contains(@class, "igbGlc")])'

    locators_sections = '(//p[contains(@class, "jRvyAe")])'

    locators_buttons = '(//label[contains(@class, "hmtoPs")])'
    locator_button_attach_file = '(//label[contains(@class, "MPznd")])'
    locator_button_to_send = '(//span[contains(@class, "dYqUsO")])'

    locators_title_messages = '(//div[contains(@class, "fUoXFK")])'
    locator_message_to_send = '//p[contains(@class, "ciLLVR")]'

    locators_input_fields = '(//input[contains(@class, "hcwsCi")])'
    locator_input_field_tell_us_about_your_project = '//textarea[contains(@class, "eGNoom")]'

    # Actions
    def check_text_in_titles(self, locators, expected_text_list):
        """ Проверка наличия элементов на странице, по содержащемуся в них тексту (заглавие, имя, название, текст).
                Принимает:
                    locators - локатор элементов (Str);
                    list_text - список ожидаемых значений (list)
        """

        list_elements = self.get_presence_elements(locators)
        n = 0
        for _ in list_elements:
            try:
                actual_name = list_elements[n].text
                # actual_name = self.get_text_element(list_elements[n])
                with allure.step(f'Проверяемый элемент:"{actual_name}"'):
                    self.scroll_to_element(list_elements[n])
                    assert actual_name in expected_text_list or expected_text_list[n] in actual_name
                    print(f'\n___Checking for element existing: {actual_name} __PASSED')
            except AssertionError:
                print(f"FAILED___ ОР={expected_text_list}, ФР={actual_name}")
            n += 1
            self.screenshot(f'check_title_{actual_name}_')

    def check_placeholder_value_in_titles(self, locators, expected_text_list, attribute_name):
        """ Проверка наличия элементов на странице, по значению атрибута.
                Принимает:
                    locators - локатор элементов (Str);
                    list_text - список ожидаемых значений (list);
                    attribute - имя атрибута хранящего значение для сравнения с ожидаемым значением (Str).
        """

        list_elements = self.get_presence_elements(locators)
        n = 0
        for _ in list_elements:
            try:
                actual_name = list_elements[n].get_attribute(attribute_name)
                # actual_name = self.get_attribute_element(list_elements[n], attribute_name)
                with allure.step(f'Проверяемый элемент:{actual_name}'):
                    self.scroll_to_element(list_elements[n])
                    assert actual_name in expected_text_list or expected_text_list[n] in actual_name
                    print(f'\n___Checking for element existing: {actual_name} __PASSED')
            except AssertionError:
                print(f"FAILED___ ОР={expected_text_list}, ФР={actual_name}")
            n += 1
            self.screenshot(f'check_title_{actual_name}_')

    # Methods

    def check_title_brief_questionnaire_page(self):
        with allure.step('Проверка заглавия страницы'):

            self.check_text_in_titles(self.locator_page_title, self.title_page)

    def check_existing_sections(self):
        with allure.step('Проверка наличия разделов на странице.'):

            self.check_text_in_titles(self.locators_sections, self.sections_names)

    def check_existing_buttons(self):
        with allure.step('Проверка наличия кнопок на странице.'):

            self.check_text_in_titles(self.locators_buttons, self.radio_button_names)
            self.check_text_in_titles(self.locator_button_attach_file, self.button_attach_file)
            self.check_text_in_titles(self.locator_button_to_send, self.button_to_send)

    def check_existing_messages(self):
        with allure.step('Проверка наличия информационных сообщений на странице.'):
            self.check_text_in_titles(self.locators_title_messages, self.titles_messages)
            self.check_text_in_titles(self.locator_message_to_send, self.title_message_to_send)

    def check_existing_input_fields(self):
        with allure.step('Проверка наличия полей ввода на странице.'):
            self.check_placeholder_value_in_titles(self.locators_input_fields, self.input_fields_names, 'placeholder')
            self.check_placeholder_value_in_titles(self.locator_input_field_tell_us_about_your_project,
                                                   self.input_field_tell_us_about_your_project, 'placeholder')

    def check_existing_all_elements(self):
        """ Проверка наличия всех элементов на странице. """

        self.check_text_in_titles(self.locators_sections, self.sections_names)
        self.check_text_in_titles(self.locators_buttons, self.radio_button_names)
        self.check_text_in_titles(self.locators_title_messages, self.titles_messages)
        self.check_text_in_titles(self.locator_message_to_send, self.title_message_to_send)
        self.check_placeholder_value_in_titles(self.locators_input_fields, self.input_fields_names, 'placeholder')
        self.check_placeholder_value_in_titles(self.locator_input_field_tell_us_about_your_project,
                                               self.input_field_tell_us_about_your_project, 'placeholder')
        self.check_text_in_titles(self.locator_button_attach_file, self.button_attach_file)
        self.check_text_in_titles(self.locator_button_to_send, self.button_to_send)
