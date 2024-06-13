import time
# from qaseio.pytest import qase
from pages.search.mol_page import CheckPage404, CheckTheCoverageMapMol
from pages.search.internet_page import CheckTheCoverageMap
from qaseio.pytest import qase
import allure


@allure.suite("Тесты поиск на МОЛ")
class TestSearch:
    @allure.title("Проверка отображения страницы 404 при запросе несуществующего URL")
    @qase.title("Проверка отображения страницы 404 при запросе несуществующего URL")
    @qase.id(454)
    def test_nonexistent_address_mol(self, driver):
        search_page = CheckPage404(driver, "https://www.moskvaonline.ru/")
        search_page.open()
        search_page.check_nonexistent_address_mol()

    @allure.title("Проверка поиска Москве")
    @qase.title("Проверка поиска Москве")
    @qase.id(455)
    def test_pagination(self, driver):
        search_page = CheckTheCoverageMapMol(driver, "https://www.moskvaonline.ru/")
        search_page.open()
        search_page.change_region_on_msk()
        search_page.check_search_gold_house()
        search_page.check_the_buttons()
        time.sleep(3)
        search_page.pangination_sharik()

    @allure.title("Проверка карты покрытия в Балашихе")
    @qase.title("Проверка карты покрытия в Балашихе")
    @qase.id(456)
    def test_map_blsh(self, driver):
        search_page = CheckTheCoverageMapMol(driver, "https://www.moskvaonline.ru/")
        search_page.open()
        search_page.change_region_on_blsh()
        search_page.check_the_coverage_map_test()
        search_page.check_the_buttons()
        time.sleep(3)
        search_page.pangination_test()


