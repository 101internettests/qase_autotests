from pages.search.pol_page import CheckPage404, CheckTheCoverageMapPol
import allure
# from qaseio.pytest import qase

@allure.suite("Тесты поиск на ПОЛ")
class TestSearch:
    def test_nonexistent_address_mol(self, driver):
        search_page = CheckPage404(driver, "https://piter-online.net/")
        search_page.open()
        search_page.check_nonexistent_address_pol()

    @allure.title("Проверка карты покрытия в Санкт-Петербурге")
    # @qase.title("Проверка карты покрытия в Санкт-Петербурге")
    def test_map_spb(self, driver):
        search_page = CheckTheCoverageMapPol(driver, "https://piter-online.net/")
        search_page.open()
        search_page.change_region_on_spb()
        search_page.check_the_coverage_map_anisimova()
        search_page.change_region_on_lenobl()
        search_page.check_the_coverage_map_vishnaykova()
        search_page.check_the_coverage_map_test()