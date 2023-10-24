import allure

from base.base_class import Base


class Checkboxes(Base):

    # Locators

    locators_buttons = '(//label[contains(@class, "hmtoPs")])'
    locators_checkbox_buttons = '(//label[contains(@class, "hmtoPs")]//input[contains(@type, "checkbox")])'
    locator_scroll_page = '//div[contains(@class, "crollbar-thumb")]'

    # Getters

    def get_status_checkbox(self, locator_checkbox):
        """ Получить текущее состояние чек-бокса.
                Возвращает:
                    False - в случае, если чек-бокс не выбран;
                    True - в случае, если чек-бокс выбран.
        """

        return self.get_clickable_element(locator_checkbox).is_selected()

    def get_checkbox(self, locator_checkbox):
        return self.get_clickable_element(locator_checkbox)

    # Methods

    def checking_status_change_checkboxes(self):
        """ Метод проверки изменения состояния чек-боксов.
                Проверки:
                 - состояние чек-боксов по умолчанию;
                 - состояние чек-боксов после нажатия на них;
                 - отключение чек-боксов.
        """
        with allure.step('Проверка чек-боксов'):
            list_elements = self.get_presence_elements(self.locators_checkbox_buttons)
            n = 0
            try:
                with allure.step('Проверка состояния чек-боксов по умолчанию. '
                                 'Проверка включения чек-боксов, после клика по ним'):
                    for _ in list_elements:
                        default_status = list_elements[n].is_selected()
                        name_element = self.get_checkbox(f'{self.locators_buttons}{[n+1]}').text
                        with allure.step(f'Проверяемый элемент:"{name_element}"'):
                            self.scroll_to_element(self.get_checkbox(f'{self.locators_buttons}{[n+1]}'))
                            self.click_on_element(f'{self.locators_buttons}{[n+1]}')
                            after_status = list_elements[n].is_selected()
                            assert default_status is False and after_status is True
                            n += 1
                    print('\n___Checking default status checkboxes. __PASSED')
                    print('\n___Checking activation checkboxes, after click. __PASSED')

            except AssertionError:
                print('\nFAILED___Checking default status checkboxes.')

            n = 0
            try:
                with allure.step('Проверка отключения чек-боксов, после клика по ним'):
                    for _ in list_elements:
                        before_status = list_elements[n].is_selected()
                        name_element = self.get_checkbox(f'{self.locators_buttons}{[n + 1]}').text
                        with allure.step(f'Проверяемый элемент:"{name_element}"'):
                            self.scroll_to_element(self.get_checkbox(f'{self.locators_buttons}{[n+1]}'))
                            self.click_on_element(f'{self.locators_buttons}{[n+1]}')
                            after_status = list_elements[n].is_selected()
                            assert before_status is True and after_status is False
                            n += 1
                    print('\n___Checking disabling checkboxes, after click. __PASSED')
            except AssertionError:
                print('\nFAILED___Checking status change checkboxes.')

    def checking_selected_checkboxes(self):
        """ Метод проверки состояния чек-боксов по умолчанию. """

        list_elements = self.get_presence_elements(self.locators_checkbox_buttons)
        n = 0
        for _ in list_elements:
            assert list_elements[n].is_selected() is False
            n += 1
        print('___Checkbox is not selected. __PASSED')
