from selenium.webdriver.common.by import By


class CoverageMapMol:
    CHOOSE_BLSH_REGION = (By.XPATH, "//a[contains(text(), 'Балашиха')]")
    CHOOSE_MSK_REGION = (By.XPATH, "//a[contains(text(), 'Москва')]")
    CHOOSE_THE_DISTRICT_BALASHIKHA = (By.XPATH, "(//a[contains(text(), 'Балашиха')])[1]")
    CHOOSE_THE_STREET_LENINA = (By.XPATH, "//a[contains(text(), 'Ленина пр-кт')]")
    CHOOSE_THE_HOUSE_16 = (By.XPATH, "(//a[contains(text(), '16')])[1]")
    CHOOSE_THE_STREET_TEST = (By.XPATH, "//a[contains(text(), 'Тестовый б-р')]")
    CHOOSE_THE_HOUSE_ONE = (By.XPATH, "(//a[contains(text(), '1')])[1]")
    CHOOSE_THE_DISTRICT_UZHNOPORTOVYI = (By.XPATH, "//a[contains(text(), 'Южнопортовый')]")
    CHOOSE_THE_STREET_SHARIK = (By.XPATH, "//a[contains(text(), 'Шарикоподшипниковская ул')]")
    CHOOSE_THE_HOUSE_11 = (By.XPATH, "(//a[contains(text(), '11')])[2]")
    SCROLL = (By.XPATH, "//div[contains(text(), 'Отзывы о Москва Онлайн на Яндекс Картах')]")
    TEXT_MOBILE = (By.XPATH, "(//h2)[6]")
    LINKING = (By.XPATH, "//h2[contains(text(), 'Другие адреса в Москве')]")
