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
    CHOOSE_TYPE_OF_CONNECTION = (By.XPATH, "//span[contains(text(), 'Тип подключения')]")
    CHOOSE_TYPE = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[1]")


class CoverageMap:
    CHOOSE_THE_REGION = (By.XPATH, "(//a[@href='/select-region'])[1]")
    WRITE_NAME_OF_REGION = (By.XPATH, "//input[@placeholder='Введите первые 3 буквы']")
    CHOOSE_CHB_REGION = (By.XPATH, "(//a[contains(text(), 'Челябинск')])[1]")
    CHOOSE_THE_COVERAGE_MAP = (By.XPATH, "//a[contains(text(), 'Карта покрытия')]")
    CHOOSE_THE_DISTRICT_KURCHATOVSKI = (By.XPATH, "//a[contains(text(), 'Курчатовский')]")
    CHOOSE_THE_STREET_TURKINA = (By.XPATH, "//a[contains(text(), 'Петра Туркина ул')]")
    CHOOSE_THE_HOUSE_THREE = (By.XPATH, "(//a[contains(text(), '3')])[1]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    CHECK_BLOCK_OF_PROVIDERS = (By.XPATH, "//div[@datatest='providers_provider_button']")
    TEXT_MOBILE = (By.XPATH,"//h2[contains(text(), 'Мобильный интернет со скоростью до 100 Мб/с на ул. Петра Туркина (Курчатовский)')]")
    CHECK_LENTEST = (By.XPATH, "//span[contains(text(), 'Выбрать провайдера')]")
    CLICK_LENTEST = (By.XPATH, "//li[contains(text(), 'Лентест')]")
    CONNECT_BUTTON = (By.XPATH, "//span[contains(text(), 'Подключить')]")
    ADRESS_BUTTON = (By.XPATH, "//a[contains(text(), 'Проверить адрес')]")
    PANGINATION_2 = (By.XPATH, "(//a[@aria-label='Переключить страницу'])[2]")
    SCROLL = (By.XPATH, "(//div[contains(text(), 'Р/мес')])[13]")
    PANGINATION_3 = (By.XPATH, "(//a[@aria-label='Переключить страницу'])[3]")
    PANGINATION_4 = (By.XPATH, "(//a[@aria-label='Переключить страницу'])[4]")
    COMPARE = (By.XPATH, "//span[contains(text(), 'сравнить')]")
    CLICK_ALL = (By.XPATH, "//div[contains(text(), 'все')]")
    PANGINATION_5 = (By.XPATH, "(//a[@aria-label='Переключить страницу'])[5]")
    PANGINATION_6 = (By.XPATH, "(//a[@aria-label='Переключить страницу'])[6]")
    PANGINATION_7 = (By.XPATH, "(//a[@aria-label='Переключить страницу'])[7]")
    PANGINATION_8 = (By.XPATH, "(//a[@aria-label='Переключить страницу'])[8]")


class GOLDEN_HOUSE:
    INPUT_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[1]")
    CLICK_ON_THE_STREET = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    INPUT_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[2]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    CHOOSE_TYPE_OF_CONNECTION = (By.XPATH, "(//span[contains(text(), 'Тип подключения')])[1]")
    CLICK_ON_TYPE_OF_CONNECTION = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[1]")
    BUTTON_SHOW_TARIFFS = (By.XPATH, "(//div[@data-test='find_tohome_button'])[1]")
    TEXT_MOBILE = (By.XPATH,"//h2[contains(text(), 'Мобильный интернет со скоростью до 100 Мбит/с и возможностью раздачи через роутер')]")
    LINKING = (By.XPATH, "//h2[contains(text(), 'Другие адреса в Челябинске')]")
    SCROLL_2 = (By.XPATH, "//div[contains(text(), 'Мобильная связь')]")
    BODY = (By.TAG_NAME, 'body')


