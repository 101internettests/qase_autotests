import time
# from qaseio.pytest import qase
import allure
from pages.urls.url_page import UrlsPage, UrlsProviderPage
from config import bot, chat_id


@allure.title("Проверка urls")
class TestCheckUrls:
    @allure.title("Проверка url на главной странице разных городов")
    # @qase.id(400)
    # @qase.title("Проверка url на главной странице разных городов")
    def test_main_urls(self, driver):
        urls = [
            "https://101internet.ru/belgorod",
            "https://101internet.ru/barnaul",
            "https://101internet.ru/chelyabinsk",
            "https://101internet.ru/kirov",
            "https://101internet.ru/vladimirskaya-oblast",
            "https://101internet.ru/penza",
            "https://101internet.ru/samara",
            "https://101internet.ru/cheboksary",
            "https://101internet.ru/perm",
            "https://101internet.ru/nizhniy-novgorod",
            "https://101internet.ru/irkutsk",
            "https://101internet.ru/belgorod/providers/rostelecom/",
            "https://101internet.ru/barnaul/providers/rostelecom/",
            "https://101internet.ru/chelyabinsk/providers/rostelecom/",
            "https://101internet.ru/kirov/providers/rostelecom/",
            "https://101internet.ru/vladimirskaya-oblast/providers/rostelecom/",
            "https://101internet.ru/penza/providers/rostelecom/",
            "https://101internet.ru/samara/providers/rostelecom/",
            "https://101internet.ru/cheboksary/providers/rostelecom/",
            "https://101internet.ru/perm/providers/rostelecom/",
            "https://101internet.ru/nizhniy-novgorod/providers/rostelecom/",
            "https://101internet.ru/irkutsk/providers/rostelecom/"

        ]

        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            try:
                links.check_the_main_number()
                print(f"Номер на рыжей кнопке на {url} успешно проверен")
            except AssertionError:
                bot.send_message(chat_id, f"На {url} проверка номера на рыжей кнопке не пройдена")

    @allure.title("Проверка url на страницах Екатеринбурга")
    # @qase.id(401)
    # @qase.title("Проверка url на страницах Екатеринбурга")
    def test_ekb_main_url(self, driver):
        urls = [
            "https://101internet.ru/ekaterinburg",
            "https://101internet.ru/ekaterinburg/providers/rostelecom/",
            "https://101internet.ru/ekaterinburg/providers/mts/",
            "https://101internet.ru/ekaterinburg/providers/beeline/",
            "https://101internet.ru/ekaterinburg/providers/dom-ru/"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            try:
                links.check_the_main_number_ekb()
                print(f"Номер на рыжей кнопке в Екатеринбурге {url} успешно проверен")
            except AssertionError:
                bot.send_message(chat_id, f"На {url} проверка номера на рыжей кнопке в Екатеринбурге не пройдена")

    @allure.title("Проверка url на страницах Новосибирска")
    # @qase.id(402)
    # @qase.title("Проверка url на страницах Новосибирска")
    def test_nov_main_url(self, driver):
        urls = [
            "https://101internet.ru/novosibirsk",
            "https://101internet.ru/novosibirsk/providers/rostelecom",
            "https://101internet.ru/novosibirsk/providers/mts"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            try:
                links.check_the_main_number_nov()
                print(f"Номер на рыжей кнопке в Новосибирске {url} успешно проверен")
            except AssertionError:
                bot.send_message(chat_id, f"На {url} проверка номера на рыжей кнопке в Новосибирске не пройдена")

    @allure.title("Проверка url на страницах Краснодара")
    # @qase.id(403)
    # @qase.title("Проверка url на страницах Краснодара")
    def test_nov_main_kras(self, driver):
        urls = [
            "https://101internet.ru/krasnodar",
            "https://101internet.ru/krasnodar/providers/rostelecom",
            "https://101internet.ru/krasnodar/providers/ttk"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            try:
                links.check_the_main_number_kras()
                print(f"Номер на рыжей кнопке в Краснодаре {url} успешно проверен")
            except AssertionError:
                bot.send_message(chat_id, f"На {url} проверка номера на рыжей кнопке в Краснодаре не пройдена")

    @allure.title("Проверка url на страницах Твери")
    # @qase.id(404)
    # @qase.title("Проверка url на страницах Твери")
    def test_nov_main_tver(self, driver):
        urls = [
            "https://101internet.ru/tver",
            "https://101internet.ru/tver/providers/rostelecom"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            try:
                links.check_the_main_number_tver()
                print(f"Номер на рыжей кнопке в Твери {url} успешно проверен")
            except AssertionError:
                bot.send_message(chat_id, f"На {url} проверка номера на рыжей кнопке в Твери не пройдена")

    @allure.title("Проверка url на страницах Ростова-на-Дону")
    # @qase.id(405)
    # @qase.title("Проверка url на страницах Ростова-на-Дону")
    def test_nov_main_rostov(self, driver):
        urls = [
            "https://101internet.ru/rostov-na-donu",
            "https://101internet.ru/rostov-na-donu/providers/dom-ru"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            try:
                links.check_the_main_number_rostov()
                print(f"Номер на рыжей кнопке в Ростове-на-Дону {url} успешно проверен")
            except AssertionError:
                bot.send_message(chat_id, f"На {url} проверка номера на рыжей кнопке в Ростове-на-Дону не пройдена")

    @allure.title("Проверка url на страницах Омска")
    # @qase.id(405)
    # @qase.title("Проверка url на страницах Омска")
    def test_nov_main_omsk(self, driver):
        urls = [
            "https://101internet.ru/omsk",
            "https://101internet.ru/omsk/providers/beeline"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            try:
                links.check_the_main_number_omsk()
                print(f"Номер на рыжей кнопке в Омске {url} успешно проверен")
            except AssertionError:
                bot.send_message(chat_id, f"На {url} проверка номера на рыжей кнопке в Омске не пройдена")

    @allure.title("Проверка url на страницах Москвы и мск. области")
    # @qase.id(406)
    # @qase.title("Проверка url на страницах Москвы и мск. области")
    def test_nov_main_msk(self, driver):
        urls = [
            "https://www.moskvaonline.ru/",
            "https://www.moskvaonline.ru/moskovskaya-oblast",
            "https://www.moskvaonline.ru/providers/rostelecom/",
            "https://www.moskvaonline.ru/moskovskaya-oblast/providers/rostelecom/",
            "https://www.moskvaonline.ru/providers/mgts/",
            "https://www.moskvaonline.ru/moskovskaya-oblast/providers/mgts/"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            try:
                links.check_the_main_number_msk()
                print(f"Номер на рыжей кнопке в Москве {url} успешно проверен")
            except AssertionError:
                bot.send_message(chat_id, f"На {url} проверка номера на рыжей кнопке в Москве не пройдена")

    @allure.title("Проверка url на страницах Санкт-Петербурга и лен. области")
    # @qase.id(406)
    # @qase.title("Проверка url на страницах Санкт-Петербурга и лен. области")
    def test_nov_main_spb(self, driver):
        urls = [
            "https://piter-online.net/",
            "https://piter-online.net/leningradskaya-oblast",
            "https://piter-online.net/providers/rostelecom/",
            "https://piter-online.net/leningradskaya-oblast/providers/rostelecom/"
        ]
        for url in urls:
            links = UrlsPage(driver, url)
            links.open()
            try:
                links.check_the_main_number_spb()
                print(f"Номер на рыжей кнопке в СПб {url} успешно проверен")
            except AssertionError:
                bot.send_message(chat_id, f"На {url} проверка номера на рыжей кнопке в СПб не пройдена")

    @allure.title("Проверка url на провайдере Ростелеком")
    # @qase.id(407)
    # @qase.title("Проверка url на провайдере Ростелеком")
    def test_rostelecom_provider(self, driver):
        urls = [
            "https://101internet.ru/belgorod/providers/rostelecom/",
            "https://101internet.ru/barnaul/providers/rostelecom/",
            "https://101internet.ru/chelyabinsk/providers/rostelecom/",
            "https://101internet.ru/kirov/providers/rostelecom/",
            "https://101internet.ru/vladimirskaya-oblast/providers/rostelecom/",
            "https://101internet.ru/penza/providers/rostelecom/",
            "https://101internet.ru/samara/providers/rostelecom/",
            "https://101internet.ru/cheboksary/providers/rostelecom/",
            "https://101internet.ru/perm/providers/rostelecom/",
            "https://101internet.ru/nizhniy-novgorod/providers/rostelecom/",
            "https://101internet.ru/irkutsk/providers/rostelecom/",
            "https://101internet.ru/ekaterinburg/providers/rostelecom/",
            "https://101internet.ru/novosibirsk/providers/rostelecom",
            "https://101internet.ru/krasnodar/providers/rostelecom",
            "https://101internet.ru/tver/providers/rostelecom"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            try:
                links.check_the_rostelecom_number()
                print(f"Проверка url на провайдере Ростелеком {url} пройдена")
            except AssertionError:
                bot.send_message(chat_id, f"Проверка на {url} url на провайдере Ростелеком не пройдена")

    @allure.title("Проверка url на провайдере Ростелеком для МОЛ")
    # @qase.id(408)
    # @qase.title("Проверка url на провайдере Ростелеком для МОЛ")
    def test_rostelecom_msk_provider(self, driver):
        urls = [
            "https://www.moskvaonline.ru/providers/rostelecom/",
            "https://www.moskvaonline.ru/moskovskaya-oblast/providers/rostelecom/"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            try:
                links.check_the_rostelecom_msk_number()
                print(f"Проверка url на провайдере Ростелеком для МОЛ {url} пройдена")
            except AssertionError:
                bot.send_message(chat_id, f"Проверка на {url} url на провайдере Ростелеком МОЛ не пройдена")

    @allure.title("Проверка url на провайдере Ростелеком для ПОЛ")
    # @qase.id(409)
    # @qase.title("Проверка url на провайдере Ростелеком для ПОЛ")
    def test_rostelecom_spb_provider(self, driver):
        urls = [
            "https://piter-online.net/providers/rostelecom/",
            "https://piter-online.net/leningradskaya-oblast/providers/rostelecom/"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            try:
                links.check_the_rostelecom_spb_number()
                print(f"Проверка url на провайдере Ростелеком для ПОЛ {url} пройдена")
            except AssertionError:
                bot.send_message(chat_id, f"Проверка на {url} url на провайдере Ростелеком ПОЛ не пройдена")

    @allure.title("Проверка url на провайдере МТС")
    # @qase.id(410)
    # @qase.title("Проверка url на провайдере МТС")
    def test_mts_provider(self, driver):
        urls = [
            "https://101internet.ru/ekaterinburg/providers/mts/",
            "https://101internet.ru/novosibirsk/providers/mts"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            try:
                links.check_the_mts_number()
                print(f"Проверка url на провайдере МТС {url} пройдена")
            except AssertionError:
                bot.send_message(chat_id, f"Проверка на {url} url на провайдере МТС не пройдена")

    @allure.title("Проверка url на провайдере Билайн")
    # @qase.id(411)
    # @qase.title("Проверка url на провайдере Билайн")
    def test_beeline_provider(self, driver):
        urls = [
            "https://101internet.ru/ekaterinburg/providers/beeline/",
            "https://101internet.ru/omsk/providers/beeline"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            try:
                links.check_the_beeline_number()
                print(f"Проверка url на провайдере Билайн {url} пройдена")
            except AssertionError:
                bot.send_message(chat_id, f"Проверка на {url} url на провайдере Билайн не пройдена")

    @allure.title("Проверка url на провайдере Дом.ру")
    # @qase.id(412)
    # @qase.title("Проверка url на провайдере Дом.ру")
    def test_domru_provider(self, driver):
        urls = [
            "https://101internet.ru/ekaterinburg/providers/dom-ru/",
            "https://101internet.ru/rostov-na-donu/providers/dom-ru"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            try:
                links.check_the_domru_number()
                print(f"Проверка url на провайдере Дом.ру {url} пройдена")
            except AssertionError:
                bot.send_message(chat_id, f"Проверка на {url} url на провайдере Дом.ру не пройдена")

    @allure.title("Проверка url на провайдере ТТК")
    # @qase.id(413)
    # @qase.title("Проверка url на провайдере ТТК")
    def test_ttk_provider(self, driver):
        urls = [
            "https://101internet.ru/krasnodar/providers/ttk"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            try:
                links.check_the_ttk_number()
                print(f"Проверка url на провайдере ТТК {url} пройдена")
            except AssertionError:
                bot.send_message(chat_id, f"Проверка на {url} url на провайдере ТТК не пройдена")

    @allure.title("Проверка url на провайдере МГТС")
    # @qase.id(414)
    # @qase.title("Проверка url на провайдере МГТС")
    def test_mgts_provider(self, driver):
        urls = [
            "https://www.moskvaonline.ru/moskovskaya-oblast/providers/mgts/",
            "https://www.moskvaonline.ru/providers/mgts/"
        ]
        for url in urls:
            links = UrlsProviderPage(driver, url)
            links.open()
            try:
                links.check_the_mgts_number()
                print(f"Проверка url на провайдере МГТС {url} пройдена")
            except AssertionError:
                bot.send_message(chat_id, f"Проверка на {url} url на провайдере МГТС не пройдена")
