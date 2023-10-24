import allure
from base.base_class import Base


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
        return radio_button.is_selected()

    # Methods

    def checking_status_change_radiobutton(self):
        """ Метод проверки изменения состояния переключателей.
                Проверки:
                 - состояние переключателя по умолчанию;
                 - состояние переключателя после нажатия на них;
        """
        with allure.step('Проверка переключателей.'):
            list_elements = self.get_presence_elements(self.locators_radio_buttons)
            n = 0
            with allure.step(
                    'Проверка состояния переключателей по умолчанию. '
                    'Проверка включения переключателей, после клика по ним'):
                for _ in list_elements:
                    default_status = self.get_status_radiobutton(list_elements[n])
                    name_element = list_elements[n].get_attribute('value')
                    with allure.step(f'Проверяемый элемент:"{name_element}"'):
                        self.scroll_to_element(self.get_clickable_element(f'{self.locators_buttons}{[n+7]}'))
                        self.click_on_element(f'{self.locators_buttons}{[n+7]}')
                        after_status = self.get_status_radiobutton(list_elements[n])
                        assert default_status is False and after_status is True, \
                            print('\nFAILED___Checking status checkboxes.')
                    n += 1
                print('\n___Checking default status radiobuttons. __PASSED')
                print('\n___Checking activation radiobuttons, after click. __PASSED')
