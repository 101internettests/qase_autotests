# import time
import allure
from locators.urls.url_locators import MainPhoneNumbersPage, ProviderPhoneNumbersPage
from pages.base_page import BasePage


class UrlsPage(BasePage):

    @allure.step("Проверь номер телефона на рыжей кнопке")
    def check_the_main_number(self):
        main = self.element_is_visible(MainPhoneNumbersPage.MAIN_NUMBER)
        assert main.text == "+7 (800) 302-32-76"

    @allure.step("Проверь номер телефона на рыжей кнопке в Екатеринбурге")
    def check_the_main_number_ekb(self):
        main = self.element_is_visible(MainPhoneNumbersPage.EKB_NUMBER)
        assert main.text == "+7 (343) 301-68-45"

    @allure.step("Проверь номер телефона на рыжей кнопке в Новосибирске")
    def check_the_main_number_nov(self):
        main = self.element_is_visible(MainPhoneNumbersPage.NOVOSIBIRSK_NUMBER)
        assert main.text == "+7 (383) 382-99-85"

    @allure.step("Проверь номер телефона на рыжей кнопке в Краснодаре")
    def check_the_main_number_kras(self):
        main = self.element_is_visible(MainPhoneNumbersPage.KRASNODAR_NUMBER)
        assert main.text == "+7 (861) 238-72-94"

    @allure.step("Проверь номер телефона на рыжей кнопке в Краснодаре")
    def check_the_main_number_tver(self):
        main = self.element_is_visible(MainPhoneNumbersPage.TVER_NUMBER)
        assert main.text == "+7 (482) 278-26-58"

    @allure.step("Проверь номер телефона на рыжей кнопке в Ростове-на-Дону")
    def check_the_main_number_rostov(self):
        main = self.element_is_visible(MainPhoneNumbersPage.ROSTOV_NA_DONU)
        assert main.text == "+7 (863) 310-39-61"

    @allure.step("Проверь номер телефона на рыжей кнопке в Омске")
    def check_the_main_number_omsk(self):
        main = self.element_is_visible(MainPhoneNumbersPage.OMSK_NUMBER)
        assert main.text == "+7 (381) 229-01-37"

    @allure.step("Проверь номер телефона на рыжей кнопке в Москве")
    def check_the_main_number_msk(self):
        main = self.element_is_visible(MainPhoneNumbersPage.MOSKVAONLINE_NUMBER)
        assert main.text == "+7 (495) 085-76-54"

    @allure.step("Проверь номер телефона на рыжей кнопке в Спб")
    def check_the_main_number_spb(self):
        main = self.element_is_visible(MainPhoneNumbersPage.PITERONLINE_NUMBER)
        assert main.text == "+7 (812) 635-33-61"


class UrlsProviderPage(BasePage):

    @allure.step("Проверь номер телефона у провайдера Ростелеком в регионах")
    def check_the_rostelecom_number(self):
        main = self.element_is_visible(ProviderPhoneNumbersPage.ROSTELECOM_NUMBER)
        assert main.text == "+7 (800) 101-17-90"

    @allure.step("Проверь номер телефона у провайдера Ростелеком в Москве")
    def check_the_rostelecom_msk_number(self):
        main = self.element_is_visible(ProviderPhoneNumbersPage.ROSTELECOM_MSK_NUMBER)
        assert main.text == "+7 (499) 372-33-55"

    @allure.step("Проверь номер телефона у провайдера Ростелеком в Санкт-Петербурге")
    def check_the_rostelecom_spb_number(self):
        main = self.element_is_visible(ProviderPhoneNumbersPage.ROSTELECOM_POL_NUMBER)
        assert main.text == "+7 (812) 605-80-89"

    @allure.step("Проверь номер телефона у провайдера МТС")
    def check_the_mts_number(self):
        main = self.element_is_visible(ProviderPhoneNumbersPage.MTS_NUMBER)
        assert main.text == "+7 (800) 101-17-95"

    @allure.step("Проверь номер телефона у провайдера Билайн")
    def check_the_beeline_number(self):
        main = self.element_is_visible(ProviderPhoneNumbersPage.BEELINE_NUMBER)
        assert main.text == "+7 (800) 101-17-81"

    @allure.step("Проверь номер телефона у провайдера Дом-ру")
    def check_the_domru_number(self):
        main = self.element_is_visible(ProviderPhoneNumbersPage.DOM_RU_NUMBER)
        assert main.text == "+7 (800) 100-90-41"

    @allure.step("Проверь номер телефона у провайдера ТТК")
    def check_the_ttk_number(self):
        main = self.element_is_visible(ProviderPhoneNumbersPage.TTK_NUMBER)
        assert main.text == "+7 (800) 707-60-52"

    @allure.step("Проверь номер телефона у провайдера МГТС")
    def check_the_mgts_number(self):
        main = self.element_is_visible(ProviderPhoneNumbersPage.MGTS)
        assert main.text == "+7 (495) 106-82-09"