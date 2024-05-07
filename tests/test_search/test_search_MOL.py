import time
# from qaseio.pytest import qase
from pages.search.mol_page import CheckPage404, CheckTheCoverageMapMol
# import random
import allure


@allure.suite("Тесты поиск на МОЛ")
class TestSearch:
    def test_nonexistent_address_mol(self, driver):
        search_page = CheckPage404(driver, "https://www.moskvaonline.ru/")
        search_page.open()
        search_page.check_nonexistent_address_mol()

    @allure.title("Проверка карты покрытия в Балашихе и Москве")
    # @qase.title("Проверка карты покрытия в Балашихе и Москве")
    def test_map_blsh(self, driver):
        search_page = CheckTheCoverageMapMol(driver, "https://www.moskvaonline.ru/")
        search_page.open()
        # search_page.change_region_on_msk()
        # search_page.check_the_coverage_map_sharik()
        search_page.change_region_on_blsh()
        search_page.check_the_coverage_map_lenina()
        # search_page.click_at_all_pagination_buttons()
        search_page.click_2()
        time.sleep(3)
        # search_page.click_3()
        # search_page.check_the_coverage_map_test()

    @allure.title("Проверка карты покрытия в Балашихе и Москве")
    # @qase.title("Проверка карты покрытия в Балашихе и Москве")
    def test_pagination(self, driver):
        search_page = CheckTheCoverageMapMol(driver, "https://www.moskvaonline.ru/")
        search_page.open()
        search_page.change_region_on_blsh()
        search_page.open_pagination_page()
        time.sleep(60)
