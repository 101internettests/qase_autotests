import allure
import time
from locators.search.locators_101 import NonexistentAddress, CoverageMap
from locators.search.locators_POL import CoverageMapPol
from pages.base_page import BasePage
from pages.search.internet_page import CheckTheCoverageMap
from selenium.webdriver import ActionChains


class CheckPage404(BasePage):
    @allure.step("Проверка несуществующего адреса")
    def check_nonexistent_address_pol(self):
        self.element_is_visible(NonexistentAddress.FIND_THE_STREET).send_keys('Олеко Дундича ул')
        self.element_is_visible(NonexistentAddress.CLICK_THE_STREET).click()
        self.element_is_visible(NonexistentAddress.FIND_THE_HOUSE).send_keys("100")
        self.element_is_visible(NonexistentAddress.CLICK_THE_HOUSE).click()
        self.element_is_visible(NonexistentAddress.CHOOSE_TYPE_OF_CONNECTION).click()
        self.element_is_visible(NonexistentAddress.CHOOSE_TYPE).click()
        self.element_is_visible(NonexistentAddress.BUTTON_SHOW_THE_RATE).click()
        text_automatic_search = self.element_is_present(NonexistentAddress.CHECK_TEXT)
        assert text_automatic_search.text == "К сожалению, автоматический поиск не дал результатов"


class CheckTheCoverageMapPol(BasePage):
    @allure.step("Выбрать регион Санкт-Петербург в хедере")
    def change_region_on_spb(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.WRITE_NAME_OF_REGION).send_keys("Санкт-Петербург")
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_SPB_REGION).click()
        time.sleep(1)

    @allure.step("Выбрать регион Ленинградскую область в хедере")
    def change_region_on_lenobl(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(CoverageMap.WRITE_NAME_OF_REGION).send_keys("Ленинградская область")
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_LENOBL_REGION).click()
        time.sleep(1)

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
            print("все ок")
        else:
            print("проверь кнопки подключения")

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
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_3):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_3).click()
            print("переход на страницу 3")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_4):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_4).click()
            print("переход на страницу 4")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_5):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_5).click()
            print("переход на страницу 5")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_6):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_6).click()
            print("переход на страницу 6")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_7):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_7).click()
            print("переход на страницу 7")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMap.PANGINATION_8):
            self.scroll()
            self.element_is_visible(CoverageMap.PANGINATION_8).click()
            print("переход на страницу 8")
            self.check_the_buttons()
        else:
            pass

    @allure.step("Проверка карты покрытия (ул Анисимова)")
    def check_the_coverage_map_anisimova(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_DISTRICT_KOLPINO).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_STREET_ANISIMOVA).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        print(num_elements)
        time.sleep(1)
        if num_elements <= 2:
            assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            self.element_is_visible(CoverageMapPol.CHOOSE_THE_HOUSE_TWO).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMapPol.CHOOSE_THE_HOUSE_TWO).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements <= 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        time.sleep(3)
        self.check_the_buttons()
        time.sleep(10)
        self.pangination()

    @allure.step("Проверка карты покрытия (ул Вишнякова)")
    def check_the_coverage_map_vishnaykova(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_DISTRICT_BOKSITOGORSK).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_STREET_VISHNYAKOVA).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        print(num_elements)
        time.sleep(1)
        if num_elements <= 2:
            assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            self.element_is_visible(CoverageMapPol.CHOOSE_THE_HOUSE_19).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMapPol.CHOOSE_THE_HOUSE_19).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements <= 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        self.element_is_visible(CoverageMap.CHECK_LENTEST).click()
        assert self.element_is_visible(CoverageMap.CLICK_LENTEST)
        time.sleep(3)
        self.check_the_buttons()
        time.sleep(10)
        self.pangination_obl()

    @allure.step("Проверка карты покрытия (линия Тестовая)")
    def check_the_coverage_map_test(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_DISTRICT_KHVOINYI).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapPol.CHOOSE_THE_STREET_TEST).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        print(num_elements)
        time.sleep(1)
        if num_elements <= 2:
            assert self.element_is_present(CoverageMapPol.TEXT_MOBILE)
            self.element_is_visible(CoverageMapPol.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMapPol.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements <= 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        self.element_is_visible(CoverageMap.CHECK_LENTEST).click()
        assert self.element_is_visible(CoverageMap.CLICK_LENTEST)
        time.sleep(3)
        self.check_the_buttons()
        time.sleep(10)
        self.pangination_obl()
