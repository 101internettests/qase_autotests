from selenium.webdriver.common.by import By
from random import randint


class WaitCallLocators:
    CHOOSE_THE_REGION = (By.XPATH, "(//a[@href='/select-region'])[1]")
    WRITE_NAME_OF_REGION = (By.XPATH, "//input[@placeholder='Введите первые 3 буквы']")
    CHOOSE_MSK_REGION = (By.XPATH, "(//a[contains(text(), 'Московская область')])[1]")
    TARIFFS_BUTTON = (By.XPATH, "(//a[@datatest='main_tariff_button'])[1]")
    SCROLL = (By.XPATH, "(//a[contains(text(), 'МТС')])[2]")
    BUTTON_WAIT_FOR_CALL = (By.XPATH, "//div[contains(text(), 'жду звонка')]")
    WRITE_TELEPHONE_NUMBER = (By.XPATH, "//input[@id='fix_callback_phone']")
    BUTTON_CALL_ME = (By.XPATH, "//div[contains(text(), 'Жду звонка')]")


class OfficeOrder:
    INTERNET_IN_OFFICE = (By.XPATH, "(//a[contains(text(), 'Интернет в офис')])[1]")
    CHOOSE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[1]")
    CLICK_ON_STREET = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    CHOOSE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[2]")
    CLICK_ON_HOUSE = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    TENDER_BUTTON = (By.XPATH, "//div[contains(text(), 'Запустить тендер')]")
    PERSON_INPUT = (By.XPATH, "//input[@datatest='business_order_input_person']")
    TELEPHON_INPUT = (By.XPATH, "//input[@datatest='business_order_input_tel']")
    BUTTON_SEND_ORDER = (By.XPATH, "(//div[contains(text(), 'Отправить заявку')])[1]")
    CHOOSE_TYPE = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[1]")


class PopUpPhoneNub:
    CHOOSE_MOSCOW = (By.XPATH, "(//a[contains(text(), 'Москва')])[1]")
    BUTTON_SHOW_TARIFFS = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")
    NUMBER_INPUT = (By.XPATH, "//input[@datatest='rates_popup1_from_quiz_input_tel']")
    NUMBER_SECOND_INPUT = (By.XPATH, "(//input[@autocomplete='tel'])[2]")
    BUTTON_SHOW_RESULTS = (By.XPATH, "//div[contains(text(), 'Показать результаты')]")
    BUTTON_SUBMIT_APPLICATION = (By.XPATH, "//div[contains(text(), 'Оставить заявку')]")
    POP_UP_TEXT = (By.XPATH, "(//img[@alt='icon']/../div)[1]")


class AddreesTariffForm:
    CLOSE_POP_UP = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    BUTTON_CONNECT = (By.XPATH, "(//div[@datatest='providers_form_inspect_connect_tariff_button'])[1]")
    INPUT_MOBILE_PHONE = (By.XPATH, "//input[@datatest='popup_tariff_order_input_tel']")
    BUTTON_SEND_APPLICATION = (By.XPATH, "//div[contains(text(), 'Отправить заявку')]")
    OPEN_PPOPUP = (By.XPATH, f"(// span[contains(text(), 'Подключить')])[{randint(0, 4)}]")
    TEXT = (By.XPATH, "(//div[contains(text(), 'телефон')])[1]")
    INPUT_NUMBER_SECOND = (By.XPATH, "//input[@datatest='providers_provider_order_input_tel']")
    BUTTON_SEND_APL_SECOND = (By.XPATH, "//div[contains(text(), 'Оставить заявку')]")
    SCROLL = (By.XPATH, "//div[contains(text(), 'Показать все детали тарифа')]")
    TARIFF_POPUP_NUM = (By.XPATH, "//input[@datatest='popup_tariff_order_input_tel']")


class OutOfTownApplication:
    SCROLL = (By.XPATH, "//a[@aria-label='Главная']")
    OUT_OF_TOWN_BUTTON = (By.XPATH, "//a[contains(text(), 'Интернет на дачу')]")
    INPUT_NAME = (By.XPATH, "(//input[@datatest='order_form_input_name'])[1]")
    INPUT_NUMBER = (By.XPATH, "(//input[@datatest='order_form_input_tel'])[1]")
    BUTTON_CONNECTION = (By.XPATH, "(//div[contains(text(), 'Подключиться')])[1]")
    TEXT_ASSERT = (By.XPATH, "(//div[contains(text(), 'Спасибо, ваша заявка на подключение принята')])[1]")


class RecentlyConnectionTariffs:
    SCROLL = (By.XPATH, "//div[contains(text(), 'Руководство пользователя.pdf')]")
    BUTTON_FIND_ADDRESS = (By.XPATH, "(//a[contains(text(), 'Поиск по адресу')])[3]")
    BUTTON_CHECK_ADDRESS = (By.XPATH, f"(//a[contains(text(), 'Проверить адрес')])[{randint(1, 4)}]")
    INPUT_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[5]")
    CLICK_ON_THE_STREET = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    INPUT_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[6]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    CHOOSE_TYPE_OF_CONNECTION = (By.XPATH, "//span[contains(text(), 'Тип подключения')]")
    CLICK_ON_TYPE_OF_CONNECTION = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[3]")
    CHECK_CONNECTION = (By.XPATH, "(//div[contains(text(), 'Проверить')])[2]")
    BUTTON_FOR_CONNECTION = (By.XPATH, "(//span[contains(text(), 'Подключить')])[3]")


class NonPartnerCardRecCon:
    PROVIDERS_BUTTON = (By.XPATH, "(//a[contains(text(), 'провайдеры')])[1]")
    CHOSE_PROVIDER_FILTER = (By.XPATH, "//input[@datatest='providers_provider_input_filter']")
    CHOSE_MOSNET = (By.XPATH, "//div[contains(text(), 'Моснет')]")
    ACCEPT_FILTER = (By.XPATH, "//div[contains(text(), 'Применить')]")
    CLICK_ON_PIC_MOSNET = (By.XPATH, "//img[@alt='Моснет']")
    INPUT_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[1]")
    CLICK_ON_THE_STREET = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[2]")
    INPUT_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[2]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "(//li[@datatest='dropdown_list_main'])[1]")
    SHOW_TARIFFS = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")
    CHOOSE_TYPE = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[2]")
    CONNECT_BUTTON = (By.XPATH, f"(//span[contains(text(), 'Подключить')])[{randint(3, 5)}]")


class ReferralUrlTariff:
    CHOSE_ABK_WELCOME = (By.XPATH, "(//div[contains(text(), 'АВК-Веллком')])[2]")
    CLICK_ON_PIC_AVK_WELCOME = (By.XPATH, "//img[@alt='АВК-Веллком']")
    CONNECT_BUTTON = (By.XPATH, f"(//span[contains(text(), 'Подключить')])[{randint(3, 5)}]")
    SCROLL = (By.XPATH, "(//a[contains(text(), 'Все тарифы')])[3]")


class WriteTariffName:
    NAME_OF_TARIFF = (By.XPATH, "//*[@id='root']/div/div[4]/div/div/div/div[1]/form/div/div[1]/span")
    NAME_OF_TARIFF_STAND = (By.XPATH, "//*[@id='root']/div/div[1]/div[4]/div[2]/div[2]/div[1]/form/div/div[1]/span")
    NAME_OF_TARIFF_B = (By.XPATH, "//h1[contains(text(), 'Тариф')]")


class OneClickLocators:
    SCROLL_MAIN_PAGE = (By.XPATH, "(//h2[contains(text(), 'Топ провайдеров домашнего интернета в ')])[2]")
    SCROLL_VOR = (By.XPATH, "(//h2[contains(text(), 'Наши партнеры в Воронеже')])[2]")
    SCROLL_FOR_POL = (By.XPATH, "(//h2[contains(text(), 'Топ провайдеров')])[2]")
    SCROLL_TOHOME_PAGE = (By.XPATH, "(//h2)[6]")
    SCROLL_TOHOME_PAGEM = (By.XPATH, "(//h2)[6]")
    NUMBER_OF_PHONE = (By.XPATH, "//input[@id='fix_callback_phone']")
    BUTTON_CHOSE_THE_TARIFF = (By.XPATH, "//div[contains(text(), 'Подобрать тариф')]")
    TEXT_CHECK = (By.XPATH, "//div[contains(text(), 'Ваша заявка принята! Мы свяжемся с вами в ближайшее время.')]")
    BUTTON_GET_CONSULTATION = (By.XPATH, "//div[contains(text(), 'Получить консультацию')]")
