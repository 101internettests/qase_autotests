from selenium.webdriver.common.by import By


class CoverageMapPol:
    CHOOSE_SPB_REGION = (By.XPATH, "//a[contains(text(), 'Санкт-Петербург')]")
    CHOOSE_THE_DISTRICT_KOLPINO = (By.XPATH, "//a[contains(text(), 'Колпино')]")
    CHOOSE_THE_STREET_ANISIMOVA = (By.XPATH, "//a[contains(text(), 'Анисимова ул')]")
    CHOOSE_THE_HOUSE_TWO = (By.XPATH, "(//a[contains(text(), '2')])[1]")
    CHOOSE_LENOBL_REGION = (By.XPATH, "//a[contains(text(), 'Ленинградская область')]")
    CHOOSE_THE_DISTRICT_BOKSITOGORSK = (By.XPATH, "//a[contains(text(), 'Бокситогорск')]")
    CHOOSE_THE_STREET_VISHNYAKOVA = (By.XPATH, "//a[contains(text(), 'Вишнякова ул')]")
    CHOOSE_THE_HOUSE_19 = (By.XPATH, "(//a[contains(text(), '19')])[1]")
    CHOOSE_THE_DISTRICT_KHVOINYI = (By.XPATH, "//a[contains(text(), 'Хвойный')]")
    CHOOSE_THE_STREET_TEST = (By.XPATH, "//a[contains(text(), 'Тестовая линия')]")
    CHOOSE_THE_HOUSE_ONE = (By.XPATH, "(//a[contains(text(), '1')])[1]")
    SCROLL = (By.XPATH, "//div[contains(text(), 'Частые вопросы')]")
    TEXT_MOBILE = (By.XPATH, "//div[contains(text(), 'МОБИЛЬНЫЙ ИНТЕРНЕТ СО СКОРОСТЬЮ')]")
    PANGINATION_2 = (By.XPATH, "//a[@href='/doma-nzl/2']")
    PANGINATION_3 = (By.XPATH, "//a[@href='/doma-nzl/3']")
    PANGINATION_4 = (By.XPATH, "//a[@href='/doma-nzl/4']")
    PANGINATION_5 = (By.XPATH, "//a[@href='/doma-nzl/5']")
    PANGINATION_2_OBL = (By.XPATH, "//a[@href='/leningradskaya-oblast/doma-nzl/2']")
    PANGINATION_3_OBL = (By.XPATH, "//a[@href='/leningradskaya-oblast/doma-nzl/3']")
    PANGINATION_4_OBL = (By.XPATH, "//a[@href='/leningradskaya-oblast/doma-nzl/4']")
    PANGINATION_5_OBL = (By.XPATH, "//a[@href='/leningradskaya-oblast/doma-nzl/5']")
    PANGINATION_6_OBL = (By.XPATH, "//a[@href='/leningradskaya-oblast/doma-nzl/6']")


