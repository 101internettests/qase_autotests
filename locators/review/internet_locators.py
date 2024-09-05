from selenium.webdriver.common.by import By


class ReviewForRegion:
    SCROLL = (By.XPATH, "//div[contains(text(), 'Общая оценка')]")
    LEAVE_FEEDBACK = (By.XPATH, "(//a[@datatest='main_allreviews_button'])[2]")
    CHOOSE_PROVIDER = (By.XPATH, "(//span[contains(text(), 'Выберите')])[1]")
    CLICK_PROVIDER = (By.XPATH, "//li[contains(text(), 'Ростелеком')]")
    CHOOSE_INTERNET = (By.XPATH, "(//span[contains(text(), 'Выберите')])[2]")
    CLICK_INTERNET = (By.XPATH, "//li[contains(text(), 'Интернет в квартиру ')]")
    CHOOSE_TIME = (By.XPATH, "//div[contains(text(), '3 месяца - 1 год')]")
    CHOOSE_SERVISE = (By.XPATH, "//div[contains(text(), 'Интернет и ТВ')]")
    CLICK_RATING = (By.XPATH, "(//div[@datatest='feedback_rating_button']/div/div/span)[1]")
    ENTER_FEEDBACK = (By.XPATH, "//textarea[@datatest='feedback_comment']")
    LEAVE_FEEDBACK_2 = (By.XPATH, "//div[@data-test='feedback_next_button']")
    CLICK_ANONIM = (By.XPATH, "//div[contains(text(), 'Анонимно')]")
    SUCCESS_POPAP = (By.XPATH, "//div[contains(text(), 'Спасибо за отзыв!')]")


class ReviewOnTheStreet:
    SCROLL = (By.XPATH, "//div[@data-test='providers_button_verify']")
    SCROLL_GOLDEN_HOUSE = (By.XPATH, "//h2[contains(text(), 'Частые вопросы')]")
    ClICK_FEEDBACK = (By.XPATH, "//a[contains(text(), 'Оставить отзыв')]")
    # LEAVE_FEEDBACK_2 = (By.XPATH, "//textarea[@aria-label='Написать отзыв']")
    LEAVE_NAME = (By.XPATH, "//input[@autocomplete='name']")
    LEAVE_FEEDBACK = (By.XPATH, "//a[contains(text(), 'Оставить отзыв')]")


class ReviewOnTheHouse:
    CLICK_PROVIDER = (By.XPATH, "//li[contains(text(), 'Ростелеком')]")
    ENTER_PHONE_NUMBER = (By.XPATH, "(//input[@id='fix_callback_phone'])[2]")


class ReviewOperator:
    SCROLL = (By.XPATH, "//span[contains(text(), 'контакты')]")
    LEAVE_FEEDBACK = (By.XPATH, "//textarea[@style = 'height: 96px;']")
    CHOOCE_OPERATOR = (By.XPATH, "//span[contains(text(), 'Оператор')]")
    CLICK_OPERATOR = (By.XPATH, "(//li[contains(text(), 'МТС')])[5]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[contains(text(), 'Спасибо за отзыв!')]")
    LEAVE_FEEDBACK_2 = (By.XPATH, "//div[contains(text(), 'Отправить отзыв')]")



class ReviewProvider:
    SCROLL = (By.XPATH, "(//a[@datatest='providers_provider_allreviews_button'])[2]")


class ReviewProviderFeedback:
    LEAVE_FEEDBACK = (By.XPATH, "//a[@datatest='providers_reviews_feedback_button']")


class ReviewMainPage:
    SCROLL = (By.XPATH, "//div[contains(text(), 'Отзыв проверен и участвует в подсчёте рейтинга провайдера')]")
    LEAVE_FEEDBACK = (By.XPATH, "(//a[@datatest='main_allreviews_button'])[1]")
