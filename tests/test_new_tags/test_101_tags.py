from pages.new_tags.internet_new_page import OneHundredMainPage
import allure


@allure.suite("Тесты теговые на 101")
class TestOneHundredInternetTags:
    @allure.title("Воронеж - тарифы, теги: 'интернет и моб. связь', 'интернет и тв и моб. связь', 'домашний интернет'")
    def test_voronezh_tags(self, driver):
        tags = OneHundredMainPage(driver, "https://101internet.ru/voronezh")
        tags.open()
        tags.open_rates()
        tags.send_application_region_tag()

    # def test_moscow_rostelecom_tags(self, driver):
    #     tags = OneHundredMainPage(driver, "https://101internet.ru/moskva/providers/rostelecom/rates/internet-i-mobilnaya-svyaz")
    #     tags.open()
    #     tags.new_application_provider()

    @allure.title("Екатеринбург - ростелеком, теги: 'интернет и моб. связь'")
    def test_ekb_rostelecom_tags(self, driver):
        tags = OneHundredMainPage(driver,
                                  "https://101internet.ru/ekaterinburg/providers/rostelecom/rates/internet-i-mobilnaya-svyaz")
        tags.open()
        tags.new_application_provider_ekb()


