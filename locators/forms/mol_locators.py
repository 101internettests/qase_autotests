from selenium.webdriver.common.by import By


class WaitMOLCallLocators:
    SCROLL = (By.XPATH, "//a[@aria-label='Главная']")
    REVIEWS = (By.XPATH, "//a[contains(text(), 'Отзывы')]")


class PopUpPhoneNubMsk:
    CHOOSE_MOSCOW = (By.XPATH, "(//a[contains(text(), 'Москва')])[1]")
    BUTTOM_SHOW_TARIFFS = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")
    NUMBER_INPUT = (By.XPATH, "//input[@datatest='rates_popup1_from_quiz_input_tel']")
    BUTTOM_SHOW_RESULTS = (By.XPATH, "//div[contains(text(), 'Показать результаты')]")


class ReferralUrlTariffMOL:
    CHOSE_MOSCOW_REGION = (By.XPATH, "//a[contains(text(), 'Московская область')]")


class WriteTariffNameMOL:
    NAME_OF_TARIFF = (By.XPATH, "//*[@id='root']/div/div[4]/div/div/div/div[1]/form/div/div[1]/span")
    NAME_OF_TARIFF_STAND = (By.XPATH, "//*[@id='root']/div/div[1]/div[4]/div[2]/div[2]/div[1]/form/div/div[1]/span")
    NAME_OF_TARIFF_B = (By.XPATH, "//h1[contains(text(), 'Тариф')]")