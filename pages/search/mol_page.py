import allure
import time
from locators.search.locators_101 import NonexistentAddress, CoverageMap
from locators.search.locators_MOL import CoverageMapMol
from pages.base_page import BasePage
from locators.search.locators_101 import GOLDEN_HOUSE
from locators.some_locator import SeoTextLocator

class CheckPage404(BasePage):
    @allure.step("Проверка несуществующего адреса")
    def check_nonexistent_address_mol(self):
        self.element_is_visible(NonexistentAddress.FIND_THE_STREET).send_keys('Липецкая ул')
        self.element_is_visible(NonexistentAddress.CLICK_THE_STREET).click()
        self.element_is_visible(NonexistentAddress.FIND_THE_HOUSE).send_keys("100")
        self.element_is_visible(NonexistentAddress.CLICK_THE_HOUSE).click()
        # self.element_is_visible(NonexistentAddress.CHOOSE_TYPE_OF_CONNECTION).click()
        # self.element_is_visible(NonexistentAddress.CHOOSE_TYPE).click()
        self.element_is_visible(NonexistentAddress.BUTTON_SHOW_THE_RATE).click()
        text_automatic_search = self.element_is_present(NonexistentAddress.CHECK_TEXT)
        assert text_automatic_search.text == "Автоматический поиск не дал результатов"


class CheckTheCoverageMapMol(BasePage):
    def close_form(self):
        # Проверяем, видим ли элемент
        popup_close_button = self.element_is_visible(SeoTextLocator.CHOOSE_THE_FORM)
        if popup_close_button:
            # Если элемент видим, то кликаем по нему
            popup_close_button.click()
        else:
            # Логируем, если элемент не найден
            print("Попап не обнаружен, пропускаем закрытие.")

    @allure.step("Выбрать регион Балашиха в хедере")
    def change_region_on_blsh(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.WRITE_NAME_OF_REGION).send_keys("Балашиха")
        time.sleep(1)
        self.element_is_visible(CoverageMapMol.CHOOSE_BLSH_REGION).click()
        time.sleep(1)

    @allure.step("Выбрать регион Москва в хедере")
    def change_region_on_msk(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.WRITE_NAME_OF_REGION).send_keys("Москва")
        time.sleep(1)
        self.element_is_visible(CoverageMapMol.CHOOSE_MSK_REGION).click()
        time.sleep(1)

    @allure.step("скролл до пангинации")
    def scroll(self):
        scroll_element = self.element_is_visible(CoverageMap.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка кнопок подключить")
    def check_the_buttons(self):
        elements = self.elements_are_visible(CoverageMap.CONNECT_BUTTON)
        time.sleep(10)
        num_elements = len(elements)
        time.sleep(10)
        print(num_elements)
        compare = self.elements_are_present(CoverageMap.COMPARE)
        time.sleep(15)
        num_compare = len(compare)
        time.sleep(15)
        print(num_compare)
        if num_elements >= num_compare:
            print("кнопки подключить найдены")
        else:
            print("проверь кнопки подключения")

    @allure.step("Скриншот страницы")
    def save_screenshot(self):
        height = self.driver.execute_script('return document.documentElement.scrollHeight')
        width = self.driver.execute_script('return document.documentElement.scrollWidth')
        self.driver.set_window_size(width, height)
        time.sleep(2)

    @allure.step("Пангинация на странице золотого дома ул Шарикоподшипниковская")
    def pangination_sharik(self):
        if self.element_is_visible(CoverageMap.PANGINATION_2):
            self.close_form()
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_2).click()
            print("переход на страницу 2")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "sharik_2.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_3):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_3).click()
            print("переход на страницу 3")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "sharik_3.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_4):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_4).click()
            print("переход на страницу 4")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "sharik_4.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_5):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_5).click()
            print("переход на страницу 5")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "sharik_5.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_6):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_6).click()
            print("переход на страницу 6")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "sharik_6.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_7):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_7).click()
            print("переход на страницу 7")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "sharik_7.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_8):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_8).click()
            print("переход на страницу 8")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "sharik_8.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass

    @allure.step("Проверка поиска (ул Шарикоподшипниковская 11)")
    def check_search_gold_house(self):
        self.element_is_visible(GOLDEN_HOUSE.INPUT_STREET).click()
        self.element_is_visible(GOLDEN_HOUSE.INPUT_STREET).send_keys("Шарикоподшипниковская ул")
        time.sleep(3)
        self.element_is_visible(GOLDEN_HOUSE.CLICK_ON_THE_STREET).click()
        time.sleep(1)
        self.element_is_visible(GOLDEN_HOUSE.INPUT_HOUSE).send_keys("11")
        time.sleep(1)
        self.element_is_visible(GOLDEN_HOUSE.CLICK_ON_THE_HOUSE).click()
        # time.sleep(2)
        # self.element_is_visible(GOLDEN_HOUSE.CHOOSE_TYPE_OF_CONNECTION).click()
        # time.sleep(2)
        # self.element_is_visible(GOLDEN_HOUSE.CLICK_ON_TYPE_OF_CONNECTION).click()
        time.sleep(2)
        self.element_is_visible(GOLDEN_HOUSE.BUTTON_SHOW_TARIFFS).click()
        time.sleep(2)
        self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        time.sleep(1)
        self.element_is_visible(CoverageMap.CLICK_ALL).click()
        time.sleep(2)
        assert self.element_is_visible(CoverageMapMol.LINKING)
        print('перелинковка найдена')
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), "sharik_1.png", allure.attachment_type.PNG)

    @allure.step("Проверка карты покрытия (б-р Тестовый)")
    def check_the_coverage_map_test(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_DISTRICT_BALASHIKHA).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_STREET_TEST).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        print('найден блок с мобильными тарифами на странице улицы')
        num_elements = len(elements)
        time.sleep(2)
        if num_elements <= 2:
            assert self.element_is_visible(CoverageMapMol.TEXT_MOBILE)
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(5)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        else:
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(5)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        self.check_the_buttons()
        time.sleep(7)
        allure.attach(self.driver.get_screenshot_as_png(), "test_1.png", allure.attachment_type.PNG)

    @allure.step("Пангинация на странице  дома б-р Тестовый")
    def pangination_test(self):
        if self.element_is_visible(CoverageMap.PANGINATION_2):
            self.scroll()
            self.close_form()
            self.element_is_visible(CoverageMap.PANGINATION_2).click()
            print("переход на страницу 2")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "test_2.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_3):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_3).click()
            print("переход на страницу 3")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "test_3.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_4):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_4).click()
            print("переход на страницу 4")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "test_4.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_5):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_5).click()
            print("переход на страницу 5")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "test_5.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_6):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_6).click()
            print("переход на страницу 6")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "test_6.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_7):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_7).click()
            print("переход на страницу 7")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "test_7.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_8):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_8).click()
            print("переход на страницу 8")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "test_8.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass