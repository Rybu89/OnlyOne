import os
import allure
from base.base_class import Base
from selenium.webdriver import ActionChains as Ac


class AttachButtons(Base):

    # Test data

    path_loading_files = '/tests/files_to_download/DrZoidberg.jpg'

    # Locators

    locator_button_attach_file_name = '//label[contains(@class, MPznd)]//span[contains(text(), "Прикрепить файл")]'
    locator_button_attach_file_input = '//label[contains(@class, MPznd)]//input[contains(@type, "file")]'
    locator_button_attach_file_label = '//div[contains(@class, "jQBsfE")]/label[contains(@class, "MPznd")]'
    locators_attached_files = '(//div[contains(@class, "uTcON")])'

    # Actions

    def loading_file(self, locator_input_button, path):
        """ Прикрепление файла.
                Принимает:
                    locator_input_button - локатор кнопки загрузки файла (Str).
                    path - путь к файлу от корневой папки проекта (Str).
        """

        os.getcwd()
        os.chdir("..")
        self.get_presence_element(locator_input_button).send_keys(f'{os.getcwd()}{path}')

    def delete_file(self, locators_attached_files):
        """ Удаление файла.
                Принимает:
                    locators_attached_files - локатор кнопки файла (Str).
        """
        self.browser.maximize_window()
        Ac(self.browser).move_to_element(self.get_visibility_element(locators_attached_files)).perform()
        self.get_clickable_element(locators_attached_files).click()

    # Methods

    def checking_button_attach_file(self):
        with allure.step('Проверить прикрепление файла'):

            """ Проверить прикрепление файла. Проверка по появлению элемента в DOM.
                    Выводит на печать:
                        FALLED___File not uploaded - в случае, если элемент не появился в DOM;
                        ___Uploaded file: {name_loading_file} __PASSED - в случае, если элемент появился в DOM.
            """

            self.loading_file(self.locator_button_attach_file_input, self.path_loading_files)
            name_loading_file = self.get_presence_element(f'{self.locators_attached_files}[1]').text
            assert self.browser.find_element('xpath', f'{self.locators_attached_files}[1]') is not None, print(
                '\n FALLED___File not uploaded')
            print(f'\n___Uploaded file: {name_loading_file} __PASSED')

    def checking_delete_attach_file(self):
        with allure.step('Проверить удаление прикрепленного файла'):

            """ Проверить удаление прикрепленного файла. Проверка по отсутствию элемента в DOM.
                    Выводит на печать:
                        FALLED___File is not deleted - в случае, если элемент обнаружен в DOM;
                        ___File is deleted __PASSED - в случае, если элемент не обнаружен в DOM.
            """

            # self.loading_file(self.locator_button_attach_file_input, self.path_loading_files)
            self.delete_file(self.locators_attached_files)
            assert self.check_exists_element_by_xpath(self.locators_attached_files) is None, print(
                '\n FALLED___File is not deleted')
            print(f'\n___File is deleted __PASSED')
