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
    #text
    locators_titles = '(//p[contains(@class, "jRvyAe")])'
    locators_radio_buttons = '(//label[contains(@class, "hmtoPs")])'
    locators_title_messages = '(//div[contains(@class, "fUoXFK")])'
    locators_input_fields = '(//input[contains(@class, "hcwsCi")])'
    #attribute
    locator_page_title = '//h2[contains(@class, "igbGlc")]'
    locator_message_to_send = '//p[contains(@class, "ciLLVR")]'
    locator_input_field_tell_us_about_your_project = '//textarea[contains(@class, "eGNoom")]'
    locator_button_attach_file = '(//label[contains(@class, "MPznd")])'
    locator_button_to_send = '(//span[contains(@class, "dYqUsO")])'

    # Actions

    def check_text_in_titles(self, list_locators_titles, list_title_name):

        """ Проверка наличия разделов на странице.
                Принимает:
                    list_titles
                    list_title_name

                """

        input_fields = self.get_visibility_elements(list_locators_titles)
        index = 1
        index2 = 0
        while index <= len(input_fields):
            locators_titles_page = f"{list_locators_titles}[{str(index)}]"
            elements = self.get_visibility_element(locators_titles_page).text
            assert list_title_name[index2] in elements
            index = index + 1
            index2 = index2 + 1
            return elements
            # print(f'\n___Checking for element existing: {elements} __PASSED')

    def check_placeholder_value_in_titles(self, list_locators_field, list_fields_name):

        input_fields = self.get_visibility_elements(list_locators_field)
        index = 1
        index2 = 0
        while index <= len(input_fields):
            locators_field_page = f"{list_locators_field}[{str(index)}]"
            elements = self.get_visibility_element(locators_field_page).get_attribute('placeholder')
            assert list_fields_name[index2] in elements
            index = index + 1
            index2 = index2 + 1
            print(f'\n___Checking for element existing: {elements} __PASSED')

    # Methods

    def check_title_brief_questionnaire_page(self):
        with allure.step('Проверка url и заглавия страницы'):
            """ Проверка заглавия страницы. """

            title = self.check_text_in_titles(self.locator_page_title, self.title_page)
            print(f'\n___Check title page ({title}) __PASSED')
            self.screenshot('check_title_brief_questionnaire_page')

    def check_existing_sections(self):
        with allure.step('Проверка наличия разделов на странице.'):
            """ Проверка наличия разделов на странице. """

            self.check_text_in_titles(self.locators_titles, self.sections_names)

    def check_existing_radio_buttons(self):
        with allure.step('Проверка наличия radio-button на странице.'):
            """ Проверка наличия radio-button на странице. """

            self.check_text_in_titles(self.locators_radio_buttons, self.radio_button_names)

    def check_existing_messages(self):
        """ Проверка наличия информационных сообщений на странице. """

        self.check_text_in_titles(self.locators_title_messages, self.titles_messages)
        self.check_text_in_titles(self.locator_message_to_send, self.title_message_to_send)

    def check_existing_input_fields(self):
        """ Проверка наличия полей ввода на странице. """

        self.check_placeholder_value_in_titles(self.locators_input_fields, self.input_fields_names)
        self.check_placeholder_value_in_titles(self.locator_input_field_tell_us_about_your_project,
                                               self.input_field_tell_us_about_your_project)

    def check_existing_buttons(self):
        """ Проверка наличия кнопок на странице. """

        self.check_text_in_titles(self.locator_button_attach_file, self.button_attach_file)
        self.check_text_in_titles(self.locator_button_to_send, self.button_to_send)

    def check_existing_all_elements(self):
        """ Проверка наличия всех элементов на странице. """

        self.check_text_in_titles(self.locators_titles, self.sections_names)
        self.check_text_in_titles(self.locators_radio_buttons, self.radio_button_names)
        self.check_text_in_titles(self.locators_title_messages, self.titles_messages)
        self.check_text_in_titles(self.locator_message_to_send, self.title_message_to_send)
        self.check_placeholder_value_in_titles(self.locators_input_fields, self.input_fields_names)
        self.check_placeholder_value_in_titles(self.locator_input_field_tell_us_about_your_project,
                                               self.input_field_tell_us_about_your_project)
        self.check_text_in_titles(self.locator_button_attach_file, self.button_attach_file)
        self.check_text_in_titles(self.locator_button_to_send, self.button_to_send)
