import allure
import time
from locators.search.locators_101 import NonexistentAddress, CoverageMap
from locators.search.locators_POL import CoverageMapPol
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class CheckPage404(BasePage):
    @allure.step("Проверка несуществующего адреса")
    def check_nonexistent_address_pol(self):
        self.element_is_visible(NonexistentAddress.FIND_THE_STREET).send_keys('Олеко Дундича ул')
        self.element_is_visible(NonexistentAddress.CLICK_THE_STREET).click()
        self.element_is_visible(NonexistentAddress.FIND_THE_HOUSE).send_keys("100")
        self.element_is_visible(NonexistentAddress.CLICK_THE_HOUSE).click()
        self.element_is_visible(NonexistentAddress.BUTTON_SHOW_THE_RATE).click()
        text_automatic_search = self.element_is_present(NonexistentAddress.CHECK_TEXT)
        assert text_automatic_search.text == "Автоматический поиск не дал результатов"


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
        scroll = self.element_is_visible(CoverageMapPol.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        time.sleep(2)
        elements = self.elements_are_visible(CoverageMap.CONNECT_BUTTON)
        time.sleep(10)
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

    @allure.step("Пангинация на странице дома в СПБ")
    def pangination(self):
        if self.element_is_visible(CoverageMapPol.PANGINATION_2):
            self.element_is_visible(CoverageMapPol.PANGINATION_2).click()
            print("переход на страницу 2")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapPol.PANGINATION_3):
            self.element_is_visible(CoverageMapPol.PANGINATION_3).click()
            print("переход на страницу 3")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapPol.PANGINATION_4):
            self.element_is_visible(CoverageMapPol.PANGINATION_4).click()
            print("переход на страницу 4")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapPol.PANGINATION_5):
            self.element_is_visible(CoverageMapPol.PANGINATION_5).click()
            print("переход на страницу 5")
            self.check_the_buttons()
        else:
            pass

    @allure.step("Пангинация на странице дома в ЛО")
    def pangination_obl(self):
        if self.element_is_visible(CoverageMapPol.PANGINATION_2_OBL):
            self.element_is_visible(CoverageMapPol.PANGINATION_2_OBL).click()
            print("переход на страницу 2")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapPol.PANGINATION_3_OBL):
            self.element_is_visible(CoverageMapPol.PANGINATION_3_OBL).click()
            print("переход на страницу 3")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapPol.PANGINATION_4_OBL):
            self.element_is_visible(CoverageMapPol.PANGINATION_4_OBL).click()
            print("переход на страницу 4")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapPol.PANGINATION_5_OBL):
            self.element_is_visible(CoverageMapPol.PANGINATION_5_OBL).click()
            print("переход на страницу 5")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapPol.PANGINATION_6_OBL):
            self.element_is_visible(CoverageMapPol.PANGINATION_6_OBL).click()
            print("переход на страницу 6")
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
