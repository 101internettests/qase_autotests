import allure
import time
from locators.search.locators_101 import SearchPage404, NonexistentAddress, CoverageMap, GOLDEN_HOUSE
from pages.base_page import BasePage


# from qaseio.pytest import qase


class CheckPage404(BasePage):
    @allure.step("Поиск текста о 404 странице")
    # @qase.title("Поиск текста о 404 странице")
    def find_text_404(self):
        text_404 = self.element_is_present(SearchPage404.SEARCH_TEXT)
        assert text_404.text == "Ой-ой-ой, мы ничего не нашли по вашему запросу! Но вы можете найти лучшие тарифы по вашему адресу. Просто введите улицу и дом"

    @allure.step("Проверка несуществующего адреса")
    # @qase.title("Проверка несуществующего адреса")
    def check_nonexistent_address(self):
        self.element_is_visible(NonexistentAddress.FIND_THE_STREET).send_keys('Петра Туркина ул')
        self.element_is_visible(NonexistentAddress.CLICK_THE_STREET).click()
        self.element_is_visible(NonexistentAddress.FIND_THE_HOUSE).send_keys("4")
        self.element_is_visible(NonexistentAddress.CLICK_THE_HOUSE).click()
        # self.element_is_visible(NonexistentAddress.CHOOSE_TYPE_OF_CONNECTION).click()
        # self.element_is_visible(NonexistentAddress.CHOOSE_TYPE).click()
        self.element_is_visible(NonexistentAddress.BUTTON_SHOW_THE_RATE).click()
        time.sleep(2)
        text_automatic_search = self.element_is_present(NonexistentAddress.CHECK_TEXT)
        assert text_automatic_search.text == "Автоматический поиск не дал результатов"


class CheckTheCoverageMap(BasePage):

    @allure.step("Выбрать регион Челябинск в хедере")
    # @qase.title("Выбрать регион Челябинск в хедере")
    def change_region_on_chb(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.WRITE_NAME_OF_REGION).send_keys("Челябинск")
        time.sleep(1)
        self.element_is_visible(CoverageMap.CHOOSE_CHB_REGION).click()
        time.sleep(1)

    @allure.step("скролл до пангинации")
    # @qase.title("скролл до пангинации")
    def scroll(self):
        scroll_element = self.element_is_visible(CoverageMap.SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    @allure.step("Проверка кнопок подключить")
    # @qase.title("Проверка кнопок подключить")
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
            print("кнопки подключить найдены")
        else:
            print("проверь кнопки подключения")

    @allure.step("Скриншот страницы")
    # @qase.title("Скриншот страницы")
    def save_screenshot(self):
        height = self.driver.execute_script('return document.documentElement.scrollHeight')
        width = self.driver.execute_script('return document.documentElement.scrollWidth')
        self.driver.set_window_size(width, height)
        time.sleep(2)

    @allure.step("Пангинация на странице дома ул Петра Туркина")
    # @qase.title("Пангинация на странице дома ул Петра Туркина")
    def pangination_turkina(self):
        if self.element_is_visible(CoverageMap.PANGINATION_2):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_2).click()
            print("переход на страницу 2")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "101_turkina_2.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_3):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_3).click()
            print("переход на страницу 3")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "101_turkina_3.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_4):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_4).click()
            print("переход на страницу 4")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "101_turkina_4.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_5):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_5).click()
            print("переход на страницу 5")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "101_turkina_5.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_6):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_6).click()
            print("переход на страницу 6")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "101_turkina_6.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_7):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_7).click()
            print("переход на страницу 7")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "101_turkina_7.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_8):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_8).click()
            print("переход на страницу 8")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "101_turkina_8.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass

    @allure.step("Проверка карты покрытия (ул Петра Туркина)")
    # @qase.title("Проверка карты покрытия (ул Петра Туркина)")
    def check_the_coverage_map_turkina(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.CHOOSE_THE_DISTRICT_KURCHATOVSKI).click()
        time.sleep(2)
        self.element_is_visible(CoverageMap.CHOOSE_THE_STREET_TURKINA).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        print('найден блок с мобильными тарифами на странице улицы')
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
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), "101_turkina_1.png", allure.attachment_type.PNG)

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
        assert self.element_is_visible(GOLDEN_HOUSE.LINKING)
        print('перелинковка найдена')
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), "batumskaya_1.png", allure.attachment_type.PNG)

    @allure.step("Пангинация на странице золотого дома ул Батумская")
    # @qase.title("Пангинация на странице золотого дома ул Батумская")
    def pangination_batymsksya(self):
        if self.element_is_visible(CoverageMap.PANGINATION_2):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_2).click()
            print("переход на страницу 2")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "batumskaya_2.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_3):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_3).click()
            print("переход на страницу 3")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "batumskaya_3.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_4):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_4).click()
            print("переход на страницу 4")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "batumskaya_4.png", allure.attachment_type.PNG)

            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_5):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_5).click()
            print("переход на страницу 5")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "batumskaya_5.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_6):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_6).click()
            print("переход на страницу 6")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "batumskaya_6.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_7):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_7).click()
            print("переход на страницу 7")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "batumskaya_7.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_8):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_8).click()
            print("переход на страницу 8")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(), "batumskaya_8.png", allure.attachment_type.PNG)
            self.check_the_buttons()
        else:
            pass

    # рекомендация при просмотре скринов:
    # посмотри скрин, чтобы хиты были всегда сверху и посмотри наличие блока с мобильными тарифами на страницы дома, если провов 2 или меньше блок должен быть
