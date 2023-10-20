import datetime
import glob
import os
import pickle
import time
import allure

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains as Ac
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")
    options.add_argument("--disable-cache")
    options.add_argument("--window-size=1920,1080")
    options.page_load_strategy = "eager"
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    s = Service()
    browser = webdriver.Chrome(options=options, service=s)

    # Getters

    def get_visibility_element(self, element_locator):

        """ Получение видимого элемента по его локатору.
                Принимает:
                 element_locator - локатор элемента (Str).
        """

        return WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.XPATH, element_locator)))

    def get_value_attribute(self, element_locator, attribute):

        """ Получение значения атрибута.
                Принимает:
                 element_locator - локатор элемента (Str);
                 attribute - имя атрибута (Str).
        """

        return WebDriverWait(self.browser, 10).until(ec.presence_of_element_located((By.XPATH, element_locator))) \
            .get_attribute(attribute)

    def get_clickable_element(self, element_locator):
        """ Получение кликабельного элемента по его локатору.
                Принимает:
                 element_locator - локатор элемента (Str).
        """

        try:
            element = WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable((By.XPATH, element_locator)))
            return element
        except:
            time.sleep(2)
            element = WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable((By.XPATH, element_locator)))
            return element

    def get_visibility_elements(self, elements_locator):

        """ Метод получения видимых элементов по их локатору.
                Принимает:
                 elements_locator - локатор элементов (Str).
        """

        return WebDriverWait(self.browser, 10) \
            .until(ec.visibility_of_all_elements_located((By.XPATH, elements_locator)))

    def get_presence_elements(self, elements_locator):

        """ Метод получения элементов присутствующих в DOM по их локатору.
                Принимает:
                 elements_locator - локатор элементов (Str).
        """

        return WebDriverWait(self.browser, 10).until(ec.presence_of_all_elements_located((By.XPATH, elements_locator)))

    def get_presence_element(self, element_locator):

        """ Метод получения элемента присутствующего в DOM по его локатору.
                Принимает:
                 element_locator - локатор элемента (Str).
        """

        try:
            element = WebDriverWait(self.browser, 10)\
                .until(ec.presence_of_element_located((By.XPATH, element_locator)))
            return element
        except:
            return None

    # Actions

    def confirmation_title(self, title, confirmation_title):

        """ Метод проверки страницы по ключевому слову.
                Принимает:
                 title - элемент страницы содержащий ключевое слово (WebElement);
                 confirmation_title - ожидаемое слово (Str).
        """

        value_word = title.text
        assert value_word == confirmation_title or confirmation_title in value_word
        return value_word

    def screenshot(self, name):

        """ Метод для снимка экрана и сохранения файла в текущую директорию.
            Автоматически проставляет дату и время снимка в название файла.
                Принимает:
                   name - имя файла для сохранения (Str).
        """

        now_date = datetime.datetime.utcnow().strftime("%H.%M.%S.%d.%m.%Y")
        # pickle.dump(self.browser.get_screenshot_as_png(), open(os.getcwd() +
        # '\\tests\\screenshots\\' f"{name}_screenshot" + now_date + '.png', "wb"))
        name_screenshot = os.getcwd() + '\\screenshots\\' + name + now_date + '.png'
        self.browser.save_screenshot(name_screenshot)

        print('___Screenshot')

    @staticmethod
    def deleting_all_screenshots():

        """ Метод для удаления всех файлов png из папки.
                Принимает:
                   answer - значения yes/YES/Yes для удаления файлов и любое другое для отмены (Str).
        """

        print('\n Удаление скриншотов')
        answer = input('Очистить папку с скриншотами? Yes/No: ')
        if answer == 'yes' or answer == 'YES' or answer == 'Yes':
            path_for_del = os.getcwd() + '\\screenshots\\'
            file_for_del = "*.png"
            filelist = glob.glob(os.path.join(path_for_del, file_for_del))
        else:
            return
        for f in filelist:
            os.remove(f)

        print('Скриншоты удалены')

    def scroll_and_release(self, element_locator, step_scroll_x_y):

        """ Метод для скроллинга элементов на странице.
                Принимает:
                    element_locator - локатор элемента (Str);
                    step_scroll_x_y - шаг по оси Х, шаг по оси Y (Int).
        """

        element = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located((By.XPATH, element_locator)))
        Ac(self.browser).move_to_element(element) \
            .click_and_hold(element) \
            .move_by_offset(*step_scroll_x_y) \
            .release() \
            .perform()

    def check_exists_element_by_xpath(self, locator):
        try:
            self.browser.find_element('xpath', locator)
        except NoSuchElementException:
            return None
        return self.browser.find_element('xpath', locator).text

    def save_cookies(self, name_file_cookie):

        """ Метод для записи cookies.
                Принимает:
                   name_file_cookie - имя сохраняемого файла (Str).
        """

        print('\n Запись cookies')
        pickle.dump(self.browser.get_cookies(), open(os.getcwd() + '\\cookies\\' + f"{name_file_cookie}_cookies", "wb"))
        print('\n Cookies записаны')

    def load_cookies(self, name_file_cookie):

        """ Метод для загрузки cookies.
                Принимает:
                   name_file_cookie - имя загружаемого файла (Str).
        """

        print('\n Загрузка cookies')
        for cookie in pickle.load(open(os.getcwd() + '\\cookies\\' + f"{name_file_cookie}_cookies", "rb")):
            self.browser.add_cookie(cookie)
        self.browser.refresh()
        print('\n Cookies загружены')
