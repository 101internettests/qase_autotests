from pages.new_tags.mol_new_page import OneHundredMainPage
import allure
from qaseio.pytest import qase


@allure.suite("Тесты теговые на МОЛ")
class TestMOLRatesTags:
    @allure.title("Москва - тарифы, теги: 'интернет и моб. связь', 'интернет и тв', 'дешевый интернет', '100мб/с'")
    @qase.title("Москва - тарифы, теги: 'интернет и моб. связь', 'интернет и тв', 'дешевый интернет', '100мб/с'")
    def test_mol_tags(self, driver):
        tags = OneHundredMainPage(driver, "https://www.moskvaonline.ru/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.send_application_region_tag()

    @allure.title("Москва - онлайм, теги: 'дешевый интернет', 'онлайн кинотеатр'")
    @qase.title("Москва - онлайм, теги: 'дешевый интернет', 'онлайн кинотеатр'")
    def test_mol_onlime_tags(self, driver):
        tags = OneHundredMainPage(driver,
                                  "https://www.moskvaonline.ru/providers/onlime/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.new_application_provider()