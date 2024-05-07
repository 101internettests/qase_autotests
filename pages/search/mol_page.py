import allure
import time
from locators.search.locators_101 import NonexistentAddress, CoverageMap
from locators.search.locators_MOL import CoverageMapMol
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class CheckPage404(BasePage):
    @allure.step("Проверка несуществующего адреса")
    def check_nonexistent_address_mol(self):
        self.element_is_visible(NonexistentAddress.FIND_THE_STREET).send_keys('Липецкая ул')
        self.element_is_visible(NonexistentAddress.CLICK_THE_STREET).click()
        self.element_is_visible(NonexistentAddress.FIND_THE_HOUSE).send_keys("100")
        self.element_is_visible(NonexistentAddress.CLICK_THE_HOUSE).click()
        self.element_is_visible(NonexistentAddress.BUTTON_SHOW_THE_RATE).click()
        text_automatic_search = self.element_is_present(NonexistentAddress.CHECK_TEXT)
        assert text_automatic_search.text == "Автоматический поиск не дал результатов"


class CheckTheCoverageMapMol(BasePage):

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

    @allure.step("Проверка кнопок подключить")
    def check_the_buttons(self):
        scroll = self.element_is_visible(CoverageMapMol.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        time.sleep(2)
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

    @allure.step("2")
    def click_2(self):
        get_all_pagination_buttons = self.elements_are_present(CoverageMapMol.ALL_PAGINATION_BUTTON)
        print(get_all_pagination_buttons)
        raise Exception("Остановка программы")
        # self.element_is_visible(CoverageMapMol.PANGINATION_2).click()
        # print("Элемент обнаружен. Отмечаем 🎉")

    def click_at_all_pagination_buttons(self):
        elements = self.elements_are_present(CoverageMapMol.ALL_PAGINATION_BUTTON)
        print('\n', elements)

    @allure.step("3")
    def click_3(self):
        if self.elements_are_present(CoverageMapMol.PANGINATION_3):
            self.element_is_present(CoverageMapMol.PANGINATION_3).click()
            print("Элемент обнаружен. Отмечаем 🎉")
        else:
            print("Элемент не найден 😞")

    @allure.step("Пангинация на странице дома в Балашихе")
    def pangination(self):
        if self.element_is_visible(CoverageMapMol.PANGINATION_2):
            self.element_is_visible(CoverageMapMol.PANGINATION_2).click()
            print("переход на страницу 2")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapMol.PANGINATION_3):
            self.element_is_visible(CoverageMapMol.PANGINATION_3).click()
            print("переход на страницу 3")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapMol.PANGINATION_4):
            self.element_is_visible(CoverageMapMol.PANGINATION_4).click()
            print("переход на страницу 4")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapMol.PANGINATION_5):
            self.element_is_visible(CoverageMapMol.PANGINATION_5).click()
            print("переход на страницу 5")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapMol.PANGINATION_6):
            self.element_is_visible(CoverageMapMol.PANGINATION_6).click()
            print("переход на страницу 6")
            self.check_the_buttons()
        else:
            pass

    @allure.step("Пангинация на странице дома в Москве")
    def pangination_msk(self):
        if self.element_is_visible(CoverageMapMol.PANGINATION_2_MSK):
            self.element_is_visible(CoverageMapMol.PANGINATION_2_MSK).click()
            print("переход на страницу 2")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapMol.PANGINATION_3_MSK):
            self.element_is_visible(CoverageMapMol.PANGINATION_3_MSK).click()
            print("переход на страницу 3")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapMol.PANGINATION_4_MSK):
            self.element_is_visible(CoverageMapMol.PANGINATION_4_MSK).click()
            print("переход на страницу 4")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapMol.PANGINATION_5_MSK):
            self.element_is_visible(CoverageMapMol.PANGINATION_5_MSK).click()
            print("переход на страницу 5")
            self.check_the_buttons()
        else:
            pass
        if self.element_is_visible(CoverageMapMol.PANGINATION_6_MSK):
            self.element_is_visible(CoverageMapMol.PANGINATION_6_MSK).click()
            print("переход на страницу 6")
            self.check_the_buttons()
        else:
            pass

    @allure.step("Проверка карты покрытия (пр-кт Ленина)")
    def check_the_coverage_map_lenina(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_DISTRICT_BALASHIKHA).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_STREET_LENINA).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        time.sleep(1)
        if num_elements <= 2:
            assert self.element_is_present(CoverageMapMol.TEXT_MOBILE)
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_16).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_16).click()
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
        time.sleep(7)
        self.pangination()

    @allure.step("Проверка карты покрытия (б-р Тестовый)")
    def check_the_coverage_map_test(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_DISTRICT_BALASHIKHA).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_STREET_TEST).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        time.sleep(2)
        if num_elements <= 2:
            assert self.element_is_visible(CoverageMapMol.TEXT_MOBILE)
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(5)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_ONE).click()
            time.sleep(5)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements <= 2:
                assert self.element_is_visible(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        self.element_is_visible(CoverageMap.CHECK_LENTEST).click()
        assert self.element_is_visible(CoverageMap.CLICK_LENTEST)
        time.sleep(3)
        self.check_the_buttons()
        time.sleep(7)
        self.pangination()

    @allure.step("Проверка карты покрытия (ул Шарикоподшипниковская)")
    def check_the_coverage_map_sharik(self):
        self.element_is_visible(CoverageMap.CHOOSE_THE_COVERAGE_MAP).click()
        time.sleep(3)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_DISTRICT_UZHNOPORTOVYI).click()
        time.sleep(1)
        self.element_is_visible(CoverageMapMol.CHOOSE_THE_STREET_SHARIK).click()
        time.sleep(1)
        elements = self.elements_are_visible(CoverageMap.CHECK_BLOCK_OF_PROVIDERS)
        num_elements = len(elements)
        time.sleep(1)
        if num_elements <= 2:
            assert self.element_is_present(CoverageMapMol.TEXT_MOBILE)
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_11).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
        elif num_elements > 2:
            self.element_is_visible(CoverageMapMol.CHOOSE_THE_HOUSE_11).click()
            time.sleep(3)
            self.element_is_visible(CoverageMap.CLOSE_THE_POPAP).click()
            if num_elements <= 2:
                assert self.element_is_present(CoverageMap.TEXT_MOBILE)
            elif num_elements > 2:
                pass
        time.sleep(3)
        self.check_the_buttons()
        time.sleep(7)
        self.pangination_msk()
