from selenium.webdriver.common.by import By
from random import randint


class DailyTagPages101Locators:
    CHOOSE_THE_REGION = (By.XPATH, "//div[@class='app19']")
    WAIT_SOME_TEXT = (By.XPATH, "//span[contains(text(), 'Выберите город или регион')]")
    WRITE_THE_CITY = (By.XPATH, "//input[@placeholder='Введите первые 3 буквы']")
    CLICK_ON_THE_CITY = (By.XPATH, "(//a[contains(text(), 'Воронеж')])[1]")
    CLICK_ON_THE_RATES = (By.XPATH, "(//a[@datatest='main_tariff_button'])[1]")


class TagPagelocators:
    TAG_INTERNET_AND_MOBILE = (By.XPATH, "//div[contains(text(), 'интернет и мобильная связь')]")
    TAG_INTERNET_TV_MOBILE = (By.XPATH, "//div[contains(text(), 'интернет+тв+мобильная связь')]")
    TAG_HOME_INTERNET = (By.XPATH, "//div[contains(text(), 'домашний интернет')]")
    TAG_INTERNET_TV = (By.XPATH, "(//div[contains(text(), 'интернет+тв')])[2]")
    TAG_CHEAP_INTERNET = (By.XPATH, "//div[contains(text(), 'дешевый интернет')]")
    TAG_100_MB = (By.XPATH, "//div[contains(text(), '100 мб/с')]")
    TAG_300_MB = (By.XPATH, "//div[contains(text(), '300 мб/с')]")
    TAG_500_MB = (By.XPATH, "//div[contains(text(), '500 мб/с')]")
    TAG_ONLINE_CINEMA = (By.XPATH, "//div[contains(text(), 'онлайн-кинотеатр')]")


class PopupFillTheAddress:
    BUTTON_CHECK_THE_ADDRESS = (By.XPATH, "//div[@datatest='button_form_inspect_connect_tariff_tag_button']")
    BUTTON_CHECK_THE_ADDRESS_SECOND = (By.XPATH, "//div[@datatest='providers_form_inspect_connect_tariff_button']")
    POP_UP_FILLED_THE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[7]")
    CLICK_ON_THE_STREET = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    POP_UP_FILLED_THE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[8]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    POP_UP_CONNECTION_TYPE = (By.XPATH, "(//span[contains(text(), 'Тип подключения')])[3]")
    POP_UP_SELECT_CONNECTION_TYPE = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[3]")
    POP_UP_BUTTON_CHECK = (By.XPATH, "(//div[contains(text(), 'Проверить')])[3]")


class PopupSuccess:
    POP_UP_SUCCESS_NUMBER = (By.XPATH, "//input[@autocomplete='tel']")
    POP_UP_NOT_SUCCESS_NUMBER = (By.XPATH, "(//input[@autocomplete='tel'])[2]")
    POP_UP_NUMBER_CLICK = (By.XPATH, "//input[@datatest='rates_popup1_from_quiz_input_tel']")
    POP_UP_SUCCESS_BUTTON = (By.XPATH, "//div[@data-test='rates_popup1_from_quiz_send_phone']")
    POP_UP_TEXT = (By.XPATH, "(//img[@alt='icon']/../div)[1]")
    BUTTON_THANK_YOU = (By.XPATH, "(//div[contains(text(), 'Спасибо')])[2]")
    CLOSE_THE_WINDOW = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    CLOSE_SUCCESS_WINDOW = (By.XPATH, "(//span[@class='icon24 icon-close'])[5]")


class LocatorsForOtherPages:
    POP_UP_FILLED_THE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[5]")
    CLICK_ON_THE_STREET = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    POP_UP_FILLED_THE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[6]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    POP_UP_CONNECTION_TYPE = (By.XPATH, "//span[contains(text(), 'Тип подключения')]")
    POP_UP_SELECT_CONNECTION_TYPE = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[3]")
    POP_UP_NOT_SUCCESS_NUMBER = (By.XPATH, "//input[@autocomplete='tel']")
    CLOSE_THE_WINDOW = (By.XPATH, "(//span[@class='icon24 icon-close'])[5]")


class AddreesTariffForm:
    CLOSE_POP_UP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    BUTTON_CONNECT = (By.XPATH, "(//div[@datatest='providers_form_inspect_connect_tariff_button'])[1]")
    INPUT_MOBILE_PHONE = (By.XPATH, "//input[@id='fix_callback_phone']")
    BUTTON_SEND_APPLICATION = (By.XPATH, "//div[contains(text(), 'Отправить заявку')]")
    OPEN_PPOPUP = (By.XPATH, f"(// span[contains(text(), 'Подключить')])[{randint(0, 4)}]")
    TEXT = (By.XPATH, "(//div[contains(text(), 'телефон')])[1]")
    INPUT_NUMBER_SECOND = (By.XPATH, "//input[@datatest='providers_provider_order_input_tel']")
    BUTTON_SEND_APL_SECOND = (By.XPATH, "//div[contains(text(), 'Оставить заявку')]")
    BUTTON_SEND_APL_THRID = (By.XPATH, "(//div[contains(text(), 'Оставить заявку')])[3]")
    SCROLL = (By.XPATH, "//div[contains(text(), 'Показать все детали тарифа')]")
    TARIFF_POPUP_NUM = (By.XPATH, "//input[@datatest='popup_tariff_order_input_tel']")
    THANKYOU_BUTTON = (By.XPATH, "//div[@data-test='give_feedback']")


class WriteTariffName:
    NAME_OF_TARIFF = (By.XPATH, "//*[@id='root']/div/div[4]/div/div/div/div[1]/form/div/div[1]/span")
    NAME_OF_TARIFF_STAND = (By.XPATH, "//*[@id='root']/div/div[1]/div[4]/div[2]/div[2]/div[1]/form/div/div[1]/span")
    NAME_OF_TARIFF_B = (By.XPATH, "//h1[contains(text(), 'Тариф')]")
