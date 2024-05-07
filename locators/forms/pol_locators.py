from selenium.webdriver.common.by import By
from random import randint


class WaitPOLCallLocators:
    CHOOSE_POL_REGION = (By.XPATH, "//a[contains(text(), 'Санкт-Петербург')]")
    SCROLL = (By.XPATH, "//a[contains(text(), 'ВайФаер')]")


class PopUpPhoneNubPOL:
    BUTTON_SHOW_TARIFFS = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")
    NUMBER_INPUT = (By.XPATH, "//input[@datatest='rates_popup1_from_quiz_input_tel']")
    BUTTON_SHOW_RESULTS = (By.XPATH, "//div[contains(text(), 'Показать результаты')]")
    POP_UP_TEXT = (By.XPATH, "(//img[@alt='icon']/../div)[1]")
    NUMBER_SECOND_INPUT = (By.XPATH, "(//input[@autocomplete='tel'])[2]")
    BUTTON_SUBMIT_APPLICATION = (By.XPATH, "//div[contains(text(), 'Оставить заявку')]")

class OutOfTownApplicationPOL:
    SCROLL = (By.XPATH, "//a[@aria-label='Главная']")


class RecentlyConnectionTariffsPol:
    SCROLL = (By.XPATH, "//a[contains(text(), 'Согласие на обработку перс.данных')]")
    BUTTON_FIND_ADDRESS = (By.XPATH, "(//a[contains(text(), 'Поиск по адресу')])[3]")
    BUTTON_CHECK_ADDRESS = (By.XPATH, f"(// a[contains(text(), 'Проверить адрес')])[{randint(1, 4)}]")
    INPUT_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[5]")
    CLICK_ON_THE_STREET = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    INPUT_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[6]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    CHOOSE_TYPE_OF_CONNECTION = (By.XPATH, "//span[contains(text(), 'Тип подключения')]")
    CLICK_ON_TYPE_OF_CONNECTION = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[3]")
    CHECK_CONNECTION = (By.XPATH, "(//div[contains(text(), 'Проверить')])[2]")


class NonPartnerPOL:
    PROVIDERS_BUTTON = (By.XPATH, "(//a[contains(text(), 'провайдеры')])[1]")
    CHOSE_PROVIDER_FILTER = (By.XPATH, "//input[@datatest='providers_provider_input_filter']")
    CHOSE_ATEL = (By.XPATH, "//div[contains(text(), 'А-ТЕЛ')]")
    ACCEPT_FILTER = (By.XPATH, "//div[contains(text(), 'Применить')]")
    CLICK_ON_PIC_ATEL= (By.XPATH, "//img[@alt='А-ТЕЛ']")
    INPUT_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[1]")
    CLICK_ON_THE_STREET = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    INPUT_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[2]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    SHOW_TARIFFS = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")
    CHOOSE_TYPE = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[2]")

class ReferralUrlTariffPOL:
    CHOSE_PACT = (By.XPATH, "//div[contains(text(), 'ПАКТ')]")
    CLICK_ON_PIC_PACT = (By.XPATH, "//img[@alt='ПАКТ']")
    SCROLL = (By.XPATH, "(//a[contains(text(), 'Все тарифы')])[3]")
    CONNECT_BUTTON = (By.XPATH, f"(//div[@datatest='providers_form_inspect_connect_tariff_button'])[{randint(2, 3)}]")


class WriteTariffNamePOL:
    NAME_OF_TARIFF = (By.XPATH, "//*[@id='root']/div/div[4]/div/div/div/div[1]/form/div/div[1]/span")
    NAME_OF_TARIFF_STAND = (By.XPATH, "//*[@id='root']/div/div[1]/div[4]/div[2]/div[2]/div[1]/form/div/div[1]/span")
    NAME_OF_TARIFF_B = (By.XPATH, "//h1[contains(text(), 'Тариф')]")