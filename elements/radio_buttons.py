from base.base_class import Base
from selenium.webdriver import ActionChains as Ac


base = Base()

class RadioButtons(Base):

    # Locators

    locators_buttons = '(//label[contains(@class, "hmtoPs")])'
    locators_radio_buttons = '(//label[contains(@class, "hmtoPs")]//input[contains(@type, "radio")])'
    locator_scroll_page = '//div[contains(@class, "crollbar-thumb")]'

    # Getters

    def get_status_radiobutton(self, radio_button):
        """ Получить текущее состояние переключателя.
                Возвращает:
                    False - в случае, если переключатель не выбран;
                    True - в случае, если переключатель выбран.
        """
        return self.get_clickable_element(radio_button).is_selected()

    # Methods

    def checking_status_change_radiobutton(self):
        """ Метод проверки изменения состояния переключателя.
                Проверки:
                 - состояние переключателя по умолчанию;
                 - состояние переключателя после нажатия на них;
                 - отключение переключателя.
        """

        list_elements = self.get_presence_elements(self.locators_radio_buttons)
        n = 0
        for _ in list_elements:
            default_status = list_elements[n].is_selected()
            Ac(self.browser)\
                .move_to_element(self.get_clickable_element(f'{self.locators_buttons}{[n+1]}'))\
                .click()\
                .perform()
            after_status = list_elements[n].is_selected()
            assert default_status is False and after_status is True
            n += 1
        n = 0
        for _ in list_elements:
            before_status = list_elements[n].is_selected()
            self.get_clickable_element(f'{self.locators_buttons}{[n+1]}').click()
            after_status = list_elements[n].is_selected()
            assert before_status is True and after_status is False
            n += 1
        print('___Checking default status radiobuttons. __PASSED')
        print('___Checking status change radiobuttons. __PASSED')

    def checking_selected_checkboxes(self):
        """ Метод проверки состояния переключателей по умолчанию. """

        list_elements = self.get_presence_elements(self.locators_radio_buttons)
        n = 0
        for _ in list_elements:
            assert list_elements[n].is_selected() is False
            n += 1
        print('___Checkbox is not selected. __PASSED')
