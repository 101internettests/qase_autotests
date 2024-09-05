from pages.review.internet_page import ReviewPageRegion, ReviewPageProvider
from qaseio.pytest import qase
import random
import allure

urls = ['https://101internet.ru/ekaterinburg/reviews',
        'https://www.moskvaonline.ru/moskovskaya-oblast/reviews']

urls_provider = ['https://101internet.ru/chelyabinsk/providers/lentest',
                 'https://www.moskvaonline.ru/providers/mts-home']

urls_street = [
    'https://101internet.ru/moskva/address/%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id1141/%D1%83%D0%BB-%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id266534',
    'https://101internet.ru/moskva/address/%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id1141/%D1%83%D0%BB-%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id266534']

urls_house = [
    'https://101internet.ru/moskva/address/%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id1141/%D1%83%D0%BB-%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id266534/d-1-id218520',
    'https://www.moskvaonline.ru/address/%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id1141/%D1%83%D0%BB-%D0%B0%D1%80%D0%B1%D0%B0%D1%82-id266534/d-1-id218520',]

urls_provider_feedback = ['https://101internet.ru/chelyabinsk/rating/rostelecom', 'https://www.moskvaonline.ru/rating/rostelecom']

urls_office = ['https://101internet.ru/chelyabinsk/orders/office', 'https://www.moskvaonline.ru/orders/office']

urls_main_page = ['https://101internet.ru/chelyabinsk', 'https://www.moskvaonline.ru']

urls_dacha = ['https://101internet.ru/chelyabinsk/orders/sat', 'https://www.moskvaonline.ru/orders/sat']

urls_operator = ['https://www.moskvaonline.ru/operatory/mts']


@allure.suite("Тесты по отзывам")
class Test101Review:

    @allure.title("Отзыв оставлен на странице региона")
    @qase.title("Отзыв оставлен на странице региона")
    @qase.id(344)
    def test_random_review(self, driver):
        random_url = random.choice(urls)
        review = ReviewPageRegion(driver, random_url)
        review.open()
        review.scroll_to_feedback_region()
        review.leave_feedback()
        print("Выбранный URL:", random_url)

    @allure.title("Отзыв оставлен на странице улицы")
    @qase.title("Отзыв оставлен на странице улицы")
    @qase.id(441)
    def test_101_rub_street(self, driver):
        random_url = random.choice(urls_street)
        review = ReviewPageRegion(driver, random_url)
        review.open()
        review.leave_the_feedback_street()
        review.leave_feedback()
        print("Выбранный URL:", random_url)

    @allure.title("Отзыв оставлен на странице золотого дома")
    @qase.title("Отзыв оставлен на странице золотого дома")
    @qase.id(442)
    def test_101_rub_house(self, driver):
        random_url = random.choice(urls_house)
        review = ReviewPageRegion(driver, random_url)
        review.open()
        review.leave_the_feedback_golden_house()
        review.leave_feedback()
        print("Выбранный URL:", random_url)

    @allure.title("Отзыв оставлен на странице оператора")
    @qase.title("Отзыв оставлен на странице оператора")
    @qase.id(443)
    def test_101_rub_operator(self, driver):
        random_url = random.choice(urls_operator)
        review = ReviewPageRegion(driver, random_url)
        review.open()
        review.leave_the_feedback_101_pub_operator()
        print("Выбранный URL:", random_url)

    @allure.title("Отзыв оставлен на странице провайдера в разделе о провайдере")
    @qase.title("Отзыв оставлен на странице провайдера в разделе о провайдере")
    @qase.id(345)
    def test_review_provider(self, driver):
        random_url = random.choice(urls_provider)
        review = ReviewPageProvider(driver, random_url)
        review.open()
        review.scroll_to_feedback_provider()
        review.leave_feedback_provider()
        print("Выбранный URL:", random_url)

    @allure.title("Отзыв оставлен на странице провайдера в разделе отзывы")
    @qase.title("Отзыв оставлен на странице провайдера в разделе отзывы")
    @qase.id(346)
    def test_review_provider_feedback(self, driver):
        random_url = random.choice(urls_provider_feedback)
        review = ReviewPageProvider(driver, random_url)
        review.open()
        review.scroll_to_feedback_provider_feedback()
        review_2 = ReviewPageRegion(driver, random_url)
        review_2.leave_feedback()
        print("Выбранный URL:", random_url)

    @allure.title("Отзыв оставлен на главной странице")
    @qase.title("Отзыв оставлен на главной странице")
    @qase.id(347)
    def test_review_main_page(self, driver):
        random_url = random.choice(urls_main_page)
        review = ReviewPageRegion(driver, random_url)
        review.open()
        review.scroll_to_feedback_maim_page()
        review.leave_feedback()
        print("Выбранный URL:", random_url)

    @allure.title("Отзыв оставлен на странице офиса")
    @qase.title("Отзыв оставлен на странице офиса")
    @qase.id(348)
    def test_review_office(self, driver):
        random_url = random.choice(urls_office)
        review = ReviewPageRegion(driver, random_url)
        review.open()
        review.scroll_to_feedback_maim_page()
        review.leave_feedback()
        print("Выбранный URL:", random_url)

    @allure.title("Отзыв оставлен на странице загородной заявки")
    @qase.title("Отзыв оставлен на странице загородной заявки")
    @qase.id(349)
    def test_review_dacha(self, driver):
        random_url = random.choice(urls_dacha)
        review = ReviewPageRegion(driver, random_url)
        review.open()
        review.scroll_to_feedback_maim_page()
        review.leave_feedback()
        print("Выбранный URL:", random_url)