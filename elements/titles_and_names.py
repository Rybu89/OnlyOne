import os
import allure
from base.base_class import Base
from selenium.webdriver import ActionChains as Ac


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
    locators_titles = '(//p[contains(@class, "jRvyAe")])'
    locators_radio_buttons = '(//label[contains(@class, "hmtoPs")])'
    locators_title_messages = '(//div[contains(@class, "fUoXFK")])'
    locators_input_fields = '(//input[contains(@class, "hcwsCi")])'
    locator_page_title = '(//h2[contains(@class, "igbGlc")])'
    locator_message_to_send = '//p[contains(@class, "ciLLVR")]'
    locator_input_field_tell_us_about_your_project = '//textarea[contains(@class, "eGNoom")]'
    locator_button_attach_file = '(//label[contains(@class, "MPznd")])'
    locator_button_to_send = '(//span[contains(@class, "dYqUsO")])'

    # Actions

    def check_text_in_titles(self, locators, list_text):

        """ Проверка наличия элементов на странице, по содержащемуся в них тексту (заглавие, имя, название, текст).
                Принимает:
                    locators - локатор элементов (Str);
                    list_text - список ожидаемых значений (list)
        """

        list_elements = self.get_presence_elements(locators)
        n = 0
        for _ in list_elements:
            name = list_elements[n].text
            Ac(self.browser).move_to_element(list_elements[n]).perform()
            assert name in list_text or list_text[n] in name
            n += 1
            self.screenshot(f'check_title_{name}_')
            print(f'\n___Checking for element existing: {name} __PASSED')

    def check_placeholder_value_in_titles(self, locators, list_text, attribute):

        """ Проверка наличия элементов на странице, по значению атрибута.
                Принимает:
                    locators - локатор элементов (Str);
                    list_text - список ожидаемых значений (list);
                    attribute - имя атрибута хранящего значение для сравнения с ожидаемым значением (Str).
        """

        list_elements = self.get_presence_elements(locators)
        n = 0
        for _ in list_elements:
            name = list_elements[n].get_attribute(attribute)
            Ac(self.browser).move_to_element(list_elements[n]).perform()
            assert name in list_text or list_text[n] in name
            n += 1
            self.screenshot(f'check_title_{name}_')
            print(f'\n___Checking for element existing: {name} __PASSED')

    # Methods

    def check_title_brief_questionnaire_page(self):
        with allure.step('Проверка заглавия страницы'):

            self.check_text_in_titles(self.locator_page_title, self.title_page)

    def check_existing_sections(self):
        with allure.step('Проверка наличия разделов на странице.'):

            self.check_text_in_titles(self.locators_titles, self.sections_names)

    def check_existing_radio_buttons(self):
        with allure.step('Проверка наличия radio-buttons на странице.'):

            self.check_text_in_titles(self.locators_radio_buttons, self.radio_button_names)

    def check_existing_messages(self):
        with allure.step('Проверка наличия информационных сообщений на странице.'):

            self.check_text_in_titles(self.locators_title_messages, self.titles_messages)
            self.check_text_in_titles(self.locator_message_to_send, self.title_message_to_send)

    def check_existing_input_fields(self):
        with allure.step('Проверка наличия полей ввода на странице.'):

            self.check_placeholder_value_in_titles(self.locators_input_fields, self.input_fields_names, 'placeholder')
            self.check_placeholder_value_in_titles(self.locator_input_field_tell_us_about_your_project,
                                                   self.input_field_tell_us_about_your_project, 'placeholder')

    def check_existing_buttons(self):
        with allure.step('Проверка наличия кнопок на странице.'):

            self.check_text_in_titles(self.locator_button_attach_file, self.button_attach_file)
            self.check_text_in_titles(self.locator_button_to_send, self.button_to_send)

    def check_existing_all_elements(self):
        """ Проверка наличия всех элементов на странице. """

        self.check_text_in_titles(self.locators_titles, self.sections_names)
        self.check_text_in_titles(self.locators_radio_buttons, self.radio_button_names)
        self.check_text_in_titles(self.locators_title_messages, self.titles_messages)
        self.check_text_in_titles(self.locator_message_to_send, self.title_message_to_send)
        self.check_placeholder_value_in_titles(self.locators_input_fields, self.input_fields_names, 'placeholder')
        self.check_placeholder_value_in_titles(self.locator_input_field_tell_us_about_your_project,
                                               self.input_field_tell_us_about_your_project, 'placeholder')
        self.check_text_in_titles(self.locator_button_attach_file, self.button_attach_file)
        self.check_text_in_titles(self.locator_button_to_send, self.button_to_send)
