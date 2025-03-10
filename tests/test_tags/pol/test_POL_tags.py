from pages.tags.pol_page import OneHundredMainPage
import allure


@allure.suite("Тесты теговые на ПОЛ")
class TestPolTags:
    @allure.title("СПб - тарифы, теги: 'интернет и моб.связь', '100мб/с', '500мб/с', 'онлайн кинотеатр'")
    def test_pol_tags(self, driver):
        tags = OneHundredMainPage(driver, "https://piter-online.net/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.send_application_region_tag()

    @allure.title("СПб - ростелеком, теги: 'интернет и моб.связь', 'домашний интернет', 'интернет и тв'")
    def test_pol_rostelecom_tags(self, driver):
        tags = OneHundredMainPage(driver,
                                  "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.megafon_fill_the_address()
