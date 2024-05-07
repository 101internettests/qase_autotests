from selenium.webdriver.common.by import By
from random import randint


class SearchPage404:
    SEARCH_TEXT = (By.XPATH,
                   "//h1[contains(text(), 'Ой-ой-ой, мы ничего не нашли по вашему запросу! Но вы можете найти лучшие тарифы по вашему адресу. Просто введите улицу и дом')]")


class NonexistentAddress:
    FIND_THE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[1]")
    CLICK_THE_STREET = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    FIND_THE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[2]")
    CLICK_THE_HOUSE = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    BUTTON_SHOW_THE_RATE = (By.XPATH, "//div[@data-test='find_tohome_button']")
    CHECK_TEXT = (By.XPATH, "//div[contains(text(), 'Автоматический поиск не дал результатов')]")


class CoverageMap:
    CHOOSE_THE_REGION = (By.XPATH, "(//a[@href='/select-region'])[1]")
    WRITE_NAME_OF_REGION = (By.XPATH, "//input[@placeholder='Введите первые 3 буквы']")
    CHOOSE_CHB_REGION = (By.XPATH, "(//a[contains(text(), 'Челябинск')])[1]")
    CHOOSE_THE_COVERAGE_MAP = (By.XPATH, "//a[@datatest='main_address_downbutton']")
    CHOOSE_THE_DISTRICT_KURCHATOVSKI = (By.XPATH, "//a[contains(text(), 'Курчатовский')]")
    CHOOSE_THE_STREET_TURKINA = (By.XPATH, "//a[contains(text(), 'Петра Туркина ул')]")
    CHOOSE_THE_HOUSE_THREE = (By.XPATH, "(//a[contains(text(), '3')])[1]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    CHOOSE_THE_DISTRICT_LENINSKI = (By.XPATH, "//a[contains(text(), 'Ленинский')]")
    CHOOSE_THE_STREET_AGALAKOVA = (By.XPATH, "//a[contains(text(), 'Агалакова ул')]")
    CHOOSE_THE_HOUSE_19 = (By.XPATH, "//a[contains(text(), '19')]")
    CHOOSE_THE_DISTRICT_KALININSKI = (By.XPATH, "//a[contains(text(), 'Калининский')]")
    CHOOSE_THE_STREET_BOLEIKO = (By.XPATH, "//a[contains(text(), 'Болейко ул')]")
    CHOOSE_THE_HOUSE_ONE = (By.XPATH, "(//a[contains(text(), '1')])[1]")
    CHOOSE_THE_HOUSE_TWO = (By.XPATH, "(//a[contains(text(), '2')])[1]")
    CHOOSE_THE_STREET_ALLEYA = (By.XPATH, "//a[contains(text(), 'Тестировщиков аллея')]")
    CHECK_BLOCK_OF_PROVIDERS = (By.XPATH, "//div[@datatest='providers_provider_button']")
    TEXT_MOBILE = (By.XPATH, "//div[contains(text(), 'МОБИЛЬНЫЙ ИНТЕРНЕТ С ВОЗМОЖНОСТЬЮ РАЗДАЧИ ЧЕРЕЗ РОУТЕР')]")
    CHECK_LENTEST = (By.XPATH, "//span[contains(text(), 'Выбрать провайдера')]")
    CLICK_LENTEST = (By.XPATH, "//li[contains(text(), 'Лентест')]")
    CONNECT_BUTTON = (By.XPATH, "//span[contains(text(), 'Подключить')]")
    ADRESS_BUTTON = (By.XPATH, "//a[contains(text(), 'Проверить адрес')]")
    PANGINATION_2 = (By.XPATH, "//a[@href='/chelyabinsk/doma-nzl/2']")
    SCROLL = (By.XPATH, "//div[contains(text(), 'Отзывы о 101 интернет на Яндекс Картах')]")
    PANGINATION_3 = (By.XPATH, "//a[@href='/chelyabinsk/doma-nzl/3']")
    PANGINATION_4 = (By.XPATH, "//a[@href='/chelyabinsk/doma-nzl/4']")
    COMPARE = (By.XPATH, "//span[contains(text(), 'сравнить')]")







