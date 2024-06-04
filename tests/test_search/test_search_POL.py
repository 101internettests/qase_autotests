from pages.search.pol_page import CheckPage404, CheckTheCoverageMapPol
import allure
import time


# from qaseio.pytest import qase

@allure.suite("Тесты поиск на ПОЛ")
class TestSearch:
    def test_nonexistent_address_mol(self, driver):
        search_page = CheckPage404(driver, "https://piter-online.net/")
        search_page.open()
        search_page.check_nonexistent_address_pol()

    @allure.title("Проверка поиска в Колпино")
    # @qase.title("Проверка поиска в Колпино")
    def test_map_kolpino(self, driver):
        search_page = CheckTheCoverageMapPol(driver, "https://piter-online.net/")
        search_page.open()
        search_page.change_region_on_kolpino()
        search_page.check_search_gold_house()
        search_page.check_the_buttons()
        time.sleep(3)
        search_page.pangination_anisimova()

    @allure.title("Проверка карты покрытия в Лен. обл.")
    # @qase.title("Проверка карты покрытия в Лен. обл.")
    def test_map_len_obl(self, driver):
        search_page = CheckTheCoverageMapPol(driver, "https://piter-online.net/")
        search_page.open()
        search_page.change_region_on_lenobl()
        search_page.check_the_coverage_map_test()
        search_page.check_the_buttons()
        time.sleep(3)
        search_page.pangination_testovaya()

