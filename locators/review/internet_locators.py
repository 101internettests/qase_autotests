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
    LEAVE_FEEDBACK_2 = (By.XPATH, "//div[contains(text(), 'Отправить отзыв')]")
    CLICK_ANONIM = (By.XPATH, "//div[contains(text(), 'Анонимно')]")
    SUCCESS_POPAP = (By.XPATH, "//div[contains(text(), 'Спасибо за отзыв!')]")


class ReviewOnTheStreet:
    SCROLL = (By.XPATH, "//div[contains(text(), 'Начать')]")
    LEAVE_FEEDBACK = (By.XPATH, "//textarea[@style='height: 95.6px;']")
    LEAVE_NAME = (By.XPATH, "//input[@autocomplete='name']")
    CHOOCE_PRIVIDER = (By.XPATH, "//span[contains(text(), 'Провайдер')]/following-sibling::input")
    # CHOOSE_ROSTELECOM = (By.XPATH, "(//input[@maxlength='500'])[3]")
    CLICK_PROVIDER = (By.XPATH, "//div[@id='forSelectField']//li[contains(text(), 'Ростелеком')]")
    LEAVE_FEEDBACK_2 = (By.XPATH, "//div[contains(text(), 'Отправить отзыв')]")
    ENTER_PHONE_NUMBER = (By.XPATH, "//input[@id='fix_callback_phone']")
    GET_101_PUB = (By.XPATH, "//div[contains(text(), 'Получить 101 руб')]")
    CLOSE_THE_POPAP = (
    By.XPATH, "//div[contains(text(), 'Дождитесь звонка, мы поможем вам подобрать интернет и начислим 101 руб')]")


class ReviewOnTheHouse:
    CLICK_PROVIDER = (By.XPATH, "//li[contains(text(), 'Ростелеком')]")
    ENTER_PHONE_NUMBER = (By.XPATH, "(//input[@id='fix_callback_phone'])[2]")


class ReviewOperator:
    SCROLL = (By.XPATH, "//span[contains(text(), 'контакты')]")
    LEAVE_FEEDBACK = (By.XPATH, "//textarea[@style = 'height: 96px;']")
    CHOOCE_OPERATOR = (By.XPATH, "//span[contains(text(), 'Оператор')]")
    CLICK_OPERATOR = (By.XPATH, "//li[contains(text(), 'МТС')]")
    CLOSE_THE_POPAP = (By.XPATH, "//div[contains(text(), 'Спасибо за отзыв!')]")


class ReviewProvider:
    SCROLL = (By.XPATH, "(//a[@datatest='providers_provider_allreviews_button'])[2]")


class ReviewProviderFeedback:
    LEAVE_FEEDBACK = (By.XPATH, "//a[@datatest='providers_reviews_feedback_button']")


class ReviewMainPage:
    SCROLL = (By.XPATH, "//div[contains(text(), 'Отзыв проверен и участвует в подсчёте рейтинга провайдера')]")
    LEAVE_FEEDBACK = (By.XPATH, "(//a[@datatest='main_allreviews_button'])[1]")
