import allure
from pages.search.internet_page import CheckPage404, CheckTheCoverageMap
import time


@allure.suite("Тесты поиск на 101")
class TestSearch:
    @allure.title("Проверка отображения страницы 404 при запросе несуществующего URL")
    def test_check_page_404(self, driver):
        urls = ['https://101internet.ru/moskva/rating/onlime/741',
                'https://www.moskvaonline.ru/moskovskaya-oblast/providers/123']
        for url in urls:
            search_page = CheckPage404(driver, url)
            search_page.open()
            search_page.find_text_404()

    @allure.title("Автоматический поиск не дал результатов при поиске с несуществующим адресом")
    def test_nonexistent_address_101(self, driver):
        search_page = CheckPage404(driver, "https://101internet.ru/chelyabinsk")
        search_page.open()
        search_page.check_nonexistent_address()

    @allure.title("Проверка карты покрытия в Челябинске")
    def test_map_chb(self, driver):
        search_page = CheckTheCoverageMap(driver, "https://101internet.ru")
        search_page.open()
        search_page.change_region_on_chb()
        search_page.check_search_gold_house()
        search_page.check_the_buttons()
        time.sleep(3)
        search_page.pangination_batymsksya()
        search_page.change_region_on_chb()
        search_page.check_the_coverage_map_turkina()
        search_page.check_the_buttons()
        time.sleep(3)
        search_page.pangination_turkina()




