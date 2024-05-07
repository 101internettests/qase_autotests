from selenium.webdriver.common.by import By


class Tagpagelocators:
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
    POP_UP_CONNECTION_TYPE = (By.XPATH, "//span[contains(text(), 'Тип подключения')]")
    POP_UP_SELECT_CONNECTION_TYPE = (By.XPATH, "(//li[contains(text(), 'В квартиру')])[3]")
    POP_UP_BUTTON_CHECK = (By.XPATH, "(//div[contains(text(), 'Проверить')])[3]")


class PopupSuccess:
    POP_UP_SUCCESS_NUMBER = (By.XPATH, "//input[@autocorrect='off']")
    POP_UP_NOT_SUCCESS_NUMBER = (By.XPATH, "(//input[@autocomplete='tel'])[2]")
    POP_UP_NUMBER_CLICK = (By.XPATH, "//span[contains(text(), 'Номер мобильного телефона')]")
    POP_UP_SUCCESS_BUTTON = (By.XPATH, "//div[@data-test='rates_popup1_from_quiz_send_phone']")
    POP_UP_TEXT = (By.XPATH, "(//img[@alt='icon']/../div)[1]")
    BUTTON_THANK_YOU = (By.XPATH, "(//div[contains(text(), 'Спасибо')])[2]")
    CLOSE_THE_WINDOW = (By.XPATH, "(//span[@class='icon24 icon-close'])[5]")
    CLOSE_SUCCESS_WINDOW = (By.XPATH, "(//span[@class='icon24 icon-close'])[5]")


class SpareTagsLocators:
    POP_UP_FILLED_THE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[5]")
    CLICK_ON_THE_STREET = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    POP_UP_FILLED_THE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[6]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    POP_UP_NOT_SUCCESS_NUMBER = (By.XPATH, "//input[@autocomplete='tel']")
    CLOSE_THE_WINDOW = (By.XPATH, "(//span[@class='icon24 icon-close'])[5]")
