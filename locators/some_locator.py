from selenium.webdriver.common.by import By


class SeoTextLocator:
    READ_MORE_BUTTON_FIRST = (By.XPATH, "//button[@class='Button_button__wliYd Button_secondary__LGYa1 Button_sm__VkQR3']")
    READ_MORE_BUTTON_SECOND = (By.XPATH, "//button[@class='Button_button__wliYd Button_blue__JwDha Button_button-adaptive__4D3Gf']")
    FAQ_READ = (By.XPATH, "(//div[@class='FAQItem_root__0pRZE'])")
    SCROLL_ONE = (
        By.XPATH, "//h2[text()='Питер Онлайн — поисковик провайдеров в Санкт-Петербурге']"
    )
    SCROLL_TWO = (By.XPATH, "//h2[text()='Отзывы о провайдерах домашнего интернета в Санкт-Петербурге']")
    SCROLL_THREE = (By.XPATH, "(//h2[text()='Частые вопросы'])")
    SCROLL_FOUR = (By.XPATH, "(//div[@class='FAQItem_root__0pRZE'])[4]")
    SCROLL_FIVE= (By.XPATH, "(//div[@class='FAQItem_root__0pRZE'])[6]")