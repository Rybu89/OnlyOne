from base.base_class import Base
from selenium.webdriver import ActionChains as Ac


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

    # Methods

    def checking_status_change_checkboxes(self):
        """ Метод проверки изменения состояния чек-боксов.
                Проверки:
                 - состояние чек-боксов по умолчанию;
                 - состояние чек-боксов после нажатия на них;
                 - отключение чек-боксов.
        """

        list_elements = self.get_presence_elements(self.locators_checkbox_buttons)
        n = 0
        try:
            for _ in list_elements:
                default_status = list_elements[n].is_selected()
                Ac(self.browser)\
                    .move_to_element(self.get_clickable_element(f'{self.locators_buttons}{[n+1]}')).perform()
                self.get_clickable_element(f'{self.locators_buttons}{[n + 1]}').click()
                after_status = list_elements[n].is_selected()
                assert default_status is False and after_status is True
                n += 1
            print('\n___Checking default status checkboxes. __PASSED')
        except:
            print('\nFAILED___Checking default status checkboxes.')

        n = 0
        try:
            for _ in list_elements:
                before_status = list_elements[n].is_selected()
                self.get_presence_element(f'{self.locators_buttons}{[n+1]}').click()
                after_status = list_elements[n].is_selected()
                assert before_status is True and after_status is False
                n += 1
            print('\n___Checking status change checkboxes. __PASSED')
        except:
            print('\nFAILED___Checking status change checkboxes.')

    def checking_selected_checkboxes(self):
        """ Метод проверки состояния чек-боксов по умолчанию. """

        list_elements = self.get_presence_elements(self.locators_checkbox_buttons)
        n = 0
        for _ in list_elements:
            assert list_elements[n].is_selected() is False
            n += 1
        print('___Checkbox is not selected. __PASSED')
