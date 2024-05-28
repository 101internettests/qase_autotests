import allure
import time
from locators.search.locators_101 import SearchPage404, NonexistentAddress, CoverageMap, GOLDEN_HOUSE
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest


class CheckPage404(BasePage):
    @allure.step("Поиск текста о 404 странице")
    def find_text_404(self):
        text_404 = self.element_is_present(SearchPage404.SEARCH_TEXT)
        assert text_404.text == "Ой-ой-ой, мы ничего не нашли по вашему запросу! Но вы можете найти лучшие тарифы по вашему адресу. Просто введите улицу и дом"

    @allure.step("Проверка несуществующего адреса")
    def check_nonexistent_address(self):
        self.element_is_visible(NonexistentAddress.FIND_THE_STREET).send_keys('Петра Туркина ул')
        self.element_is_visible(NonexistentAddress.CLICK_THE_STREET).click()
        self.element_is_visible(NonexistentAddress.FIND_THE_HOUSE).send_keys("4")
        self.element_is_visible(NonexistentAddress.CLICK_THE_HOUSE).click()
        self.element_is_visible(NonexistentAddress.CHOOSE_TYPE_OF_CONNECTION).click()
        self.element_is_visible(NonexistentAddress.CHOOSE_TYPE).click()
        self.element_is_visible(NonexistentAddress.BUTTON_SHOW_THE_RATE).click()
        time.sleep(2)
        text_automatic_search = self.element_is_present(NonexistentAddress.CHECK_TEXT)
        assert text_automatic_search.text == "К сожалению, автоматический поиск не дал результатов"


class CheckTheCoverageMap(BasePage):

    @allure.step("Выбрать регион Челябинск в хедере")
    def change_region_on_chb(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.WRITE_NAME_OF_REGION).send_keys("Челябинск")
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_CHB_REGION).click()
        time.sleep(1)

    @allure.step("скролл до пангинации")
    def scroll(self):
        scroll_element = self.element_is_visible(CoverageMap.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Пангинация на странице дома")
    def pangination(self):
        if self.element_is_visible(CoverageMap.PANGINATION_2):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_2).click()
            print("переход на страницу 2")
            time.sleep(3)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_3):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_3).click()
            print("переход на страницу 3")
            time.sleep(3)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_4):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_4).click()
            print("переход на страницу 4")
            time.sleep(3)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_5):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_5).click()
            print("переход на страницу 5")
            time.sleep(3)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_6):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_6).click()
            print("переход на страницу 6")
            time.sleep(3)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_7):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_7).click()
            print("переход на страницу 7")
            time.sleep(3)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_8):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_8).click()
            print("переход на страницу 8")
            time.sleep(3)
            self.check_the_buttons()
        else:
            pass

    @allure.step("Проверка карты покрытия (ул Петра Туркина)")
    def check_the_coverage_map_turkina(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT_KURCHATOVSKI).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET_TURKINA).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        print('найден блок с мобильными тарифами')
        num_elements = len(elements)
        time.sleep(2)
        if num_elements <= 2:
            assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_THREE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMap.CHOOSE_THE_HOUSE_THREE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        self.element_is_visible(CoverageMap.CLICK_ALL).click()
        self.element_is_visible(CoverageMap.CHECK_LENTEST).click()
        assert self.element_is_visible(CoverageMap.CLICK_LENTEST)
        # elements = self.element_is_visible(GOLDEN_HOUSE.TEXT_MOBILE).text
        # time.sleep(2)
        # if elements == ('Мобильный интернет со скоростью до 100 Мбит/с и возможностью раздачи через роутер'):
        #     print('найден блок с мобильными тарифами')
        # elif elements != ('Мобильный интернет со скоростью до 100 Мбит/с и возможностью раздачи через роутер'):
        #     print('провайдеров больше 2, блока с мобильными тарифами нет')
        #     pass
        self.check_the_buttons()

    @allure.step("Проверка поиска (ул Батумская 9а)")
    def check_search_gold_house(self):
        self.element_is_visible(GOLDEN_HOUSE.INPUT_STREET).click()
        self.element_is_visible(GOLDEN_HOUSE.INPUT_STREET).send_keys("Батумская ул")
        time.sleep(3)
        self.element_is_visible(GOLDEN_HOUSE.CLICK_ON_THE_STREET).click()
        time.sleep(1)
        self.element_is_visible(GOLDEN_HOUSE.INPUT_HOUSE).send_keys("9а")
        time.sleep(1)
        self.element_is_visible(GOLDEN_HOUSE.CLICK_ON_THE_HOUSE).click()
        time.sleep(2)
        self.element_is_visible(GOLDEN_HOUSE.CHOOSE_TYPE_OF_CONNECTION).click()
        time.sleep(2)
        self.element_is_visible(GOLDEN_HOUSE.CLICK_ON_TYPE_OF_CONNECTION).click()
        time.sleep(2)
        self.element_is_visible(GOLDEN_HOUSE.BUTTON_SHOW_TARIFFS).click()
        self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CLICK_ALL).click()
        time.sleep(2)
        assert self.element_is_visible(GOLDEN_HOUSE.LINKING)
        print('перелинковка найдена')
        time.sleep(2)
        # try:
        #     self.element_is_visible(GOLDEN_HOUSE.TEXT_MOBILE)
        # except NoSuchElementException:
        #     return False
        # print('нет')
        # return True
        # print('да')
        self.check_the_buttons()

    @allure.step("Проверка кнопок подключить")
    def check_the_buttons(self):
        elements = self.elements_are_visible(CoverageMap.CONNECT_BUTTON)
        num_elements = len(elements)
        time.sleep(10)
        print(num_elements)
        compare = self.elements_are_present(CoverageMap.COMPARE)
        time.sleep(10)
        num_compare = len(compare)
        time.sleep(10)
        print(num_compare)
        if num_elements >= num_compare:
            print("все ок")
        else:
            print("проверь кнопки подключения")
