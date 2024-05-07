from selenium.webdriver.common.by import By


class MainPhoneNumbersPage:
    MAIN_NUMBER = (By.XPATH, "(//div[contains(text(), '+7 (800) 302-32-76')])[1]")
    EKB_NUMBER = (By.XPATH, "(//div[contains(text(), '+7 (343) 301-68-45')])[1]")
    NOVOSIBIRSK_NUMBER = (By.XPATH, "(//div[contains(text(), '+7 (383) 382-99-85')])[1]")
    KRASNODAR_NUMBER = (By.XPATH, "(//div[contains(text(), '+7 (861) 238-72-94')])[1]")
    TVER_NUMBER = (By.XPATH, "(//div[contains(text(), '+7 (482) 278-26-58')])[1]")
    ROSTOV_NA_DONU = (By.XPATH, "(//div[contains(text(), '+7 (863) 310-39-61')])[1]")
    OMSK_NUMBER = (By.XPATH, "(//div[contains(text(), '+7 (381) 229-01-37')])[1]")
    MOSKVAONLINE_NUMBER = (By.XPATH, "(//div[contains(text(), '+7 (495) 085-76-54')])[1]")
    PITERONLINE_NUMBER = (By.XPATH, "(//div[contains(text(), '+7 (812) 635-33-61')])[1]")


class ProviderPhoneNumbersPage:
    ROSTELECOM_NUMBER = (By.XPATH, "(//a[contains(text(), '+7 (800) 101-17-90')])[1]")
    ROSTELECOM_MSK_NUMBER = (By.XPATH, "(//a[contains(text(), '+7 (499) 372-33-55')])[1]")
    ROSTELECOM_POL_NUMBER = (By.XPATH, "(//a[contains(text(), '+7 (812) 605-80-89')])[1]")
    MTS_NUMBER = (By.XPATH, "(//a[contains(text(), '+7 (800) 101-17-95')])[1]")
    BEELINE_NUMBER = (By.XPATH, "(//a[contains(text(), '+7 (800) 101-17-81')])[1]")
    DOM_RU_NUMBER = (By.XPATH, "(//a[contains(text(), '+7 (800) 100-90-41')])[1]")
    TTK_NUMBER = (By.XPATH, "(//a[contains(text(), '+7 (800) 707-60-52')])[1]")
    MGTS = (By.XPATH, "(//a[contains(text(), '+7 (495) 106-82-09')])[1]")
