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
    TEXT_MOBILE = (By.XPATH, "//h2[contains(text(), 'Мобильный интернет со скоростью до 100 Мб/с на линия. Тестовая (Хвойный)')]")
    LINKING = (By.XPATH, "//h2[contains(text(), 'Другие адреса в Санкт-Петербурге')]")


