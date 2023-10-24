import allure
from base.base_class import Base


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
        with allure.step('Прикрепить файл.'):
            # os.getcwd()
            # os.chdir("..")
            # self.get_presence_element(locator_input_button).send_keys(f'{os.getcwd()}{path}')
            self.go_to_current_directory()
            self.go_to_up_directory()
            self.enter_path_from_current_directory(locator_input_button, path)

    def delete_attached_file(self, locators_attached_file):
        """ Удаление файла.
                Принимает:
                    locators_attached_files - локатор кнопки файла (Str).
        """
        # self.browser.maximize_window()
        # Ac(self.browser).move_to_element(self.get_visibility_element(locators_attached_file)).perform()
        # self.get_clickable_element(locators_attached_file).click()
        with allure.step('Удалить прикрепленный файл.'):
            self.scroll_to_element(self.get_visibility_element(locators_attached_file))
            self.click_on_element(locators_attached_file)

    # Methods

    def checking_button_attach_file(self):
        """ Проверить прикрепление файла. Проверка по появлению элемента в DOM.
                    Выводит на печать:
                        FALLED___File not uploaded - в случае, если элемент не появился в DOM;
                        ___Uploaded file: {name_loading_file} __PASSED - в случае, если элемент появился в DOM.
        """

        with allure.step('Проверка кнопки прикрепления файла'):
            self.loading_file(self.locator_button_attach_file_input, self.path_loading_files)
            name_loading_file = self.get_text_element(f'{self.locators_attached_files}[1]')
            # name_loading_file = self.get_presence_element(f'{self.locators_attached_files}[1]').text
            # assert self.browser.find_element('xpath', f'{self.locators_attached_files}[1]') is not None, print(
            #     '\n FALLED___File not uploaded')
            assert self.get_visibility_element(f'{self.locators_attached_files}[1]') is not None, print(
                '\n FALLED___File not uploaded')
            print(f'\n___Uploaded file: {name_loading_file} __PASSED')

    def checking_button_delete_attach_file(self):
        """ Проверить удаление прикрепленного файла. Проверка по отсутствию элемента в DOM.
                Выводит на печать:
                   FALLED___File is not deleted - в случае, если элемент обнаружен в DOM;
                   ___File is deleted __PASSED - в случае, если элемент не обнаружен в DOM.
        """

        with allure.step('Проверка кнопки удаления прикрепленного файла'):
            # self.loading_file(self.locator_button_attach_file_input, self.path_loading_files)
            self.delete_attached_file(self.locators_attached_files)
            assert self.check_exists_element_by_xpath(self.locators_attached_files) is None, print(
                '\n FALLED___File is not deleted')
            print(f'\n___File is deleted __PASSED')
