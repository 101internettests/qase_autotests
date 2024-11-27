import os
import uuid
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from pages.page import TestsSeoCheck
HEADLESS = os.getenv("HEADLESS") == "True"


class TestSearChrome:
    def test_check_search_chrome(self, driver):
        if HEADLESS:
            driver.set_window_size(1920, 1080)
        else:
            driver.maximize_window()

        urls = [
            "https://piter-online.net/",
            # "https://101inter:test101@stage.next.piter-online.net/orders/tohome",
            # "https://101inter:test101@stage.next.piter-online.net/address",
            # "https://101inter:test101@stage.next.piter-online.net/address/%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D1%81%D0%BA-id1250",
            # "https://101inter:test101@stage.next.piter-online.net/address/%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D1%81%D0%BA-id1250/%D1%83%D0%BB-2-%D1%8F-%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%84%D0%BB%D0%BE%D1%82%D1%81%D0%BA%D0%B0%D1%8F-id295159",
            # "https://101inter:test101@stage.next.piter-online.net/dom/ul-2-yakrasnoflotskaya-d-6-k2a-id1018691",
            # "https://101inter:test101@stage.next.piter-online.net/leningradskaya-oblast/doma-nzl?house_id=4270758",
            # "https://101inter:test101@stage.next.piter-online.net/all-districts",
            # "https://101inter:test101@stage.next.piter-online.net/rating",
            # "https://101inter:test101@stage.next.piter-online.net/reviews",
            # "https://101inter:test101@stage.next.piter-online.net/rating/mts",
            # "https://101inter:test101@stage.next.piter-online.net/feedback",
            # "https://101inter:test101@stage.next.piter-online.net/providers",
            # "https://101inter:test101@stage.next.piter-online.net/providers/dom-ru",
            # "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom",
            # "https://101inter:test101@stage.next.piter-online.net/providers/tele-2",
            # "https://101inter:test101@stage.next.piter-online.net/providers/mts",
            # "https://101inter:test101@stage.next.piter-online.net/providers/megafon",
            # "https://101inter:test101@stage.next.piter-online.net/providers/beeline",
            # "https://101inter:test101@stage.next.piter-online.net/providers/akado-neva",
            # "https://101inter:test101@stage.next.piter-online.net/providers/awanti",
            # "https://101inter:test101@stage.next.piter-online.net/providers/dom-ru/rates",
            # "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates",
            # "https://101inter:test101@stage.next.piter-online.net/providers/tele-2/rates",
            # "https://101inter:test101@stage.next.piter-online.net/providers/mts/rates",
            # "https://101inter:test101@stage.next.piter-online.net/providers/megafon/rates",
            # "https://101inter:test101@stage.next.piter-online.net/providers/beeline/rates",
            # "https://101inter:test101@stage.next.piter-online.net/providers/akado-neva/rates",
            # "https://101inter:test101@stage.next.piter-online.net/providers/dom-ru/rates/domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates/domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/tele-2/rates/domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/mts/rates/domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/megafon/rates/domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/beeline/rates/domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/akado-neva/rates/domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/dom-ru/rates/internet-i-tv",
            # "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates/internet-i-tv",
            # "https://101inter:test101@stage.next.piter-online.net/providers/beeline/rates/internet-i-tv",
            # "https://101inter:test101@stage.next.piter-online.net/providers/akado-neva/rates/internet-i-tv",
            # "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates/internet-tv-mobile",
            # "https://101inter:test101@stage.next.piter-online.net/providers/tele-2/rates/internet-tv-mobile",
            # "https://101inter:test101@stage.next.piter-online.net/providers/mts/rates/internet-tv-mobile",
            # "https://101inter:test101@stage.next.piter-online.net/providers/megafon/rates/internet-tv-mobile",
            # "https://101inter:test101@stage.next.piter-online.net/providers/beeline/rates/internet-tv-mobile",
            # "https://101inter:test101@stage.next.piter-online.net/providers/wifire/rates/internet-tv-mobile",
            # "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates/internet-i-mobilnaya-svyaz",
            # "https://101inter:test101@stage.next.piter-online.net/providers/tele-2/rates/internet-i-mobilnaya-svyaz",
            # "https://101inter:test101@stage.next.piter-online.net/providers/mts/rates/internet-i-mobilnaya-svyaz",
            # "https://101inter:test101@stage.next.piter-online.net/providers/megafon/rates/internet-i-mobilnaya-svyaz",
            # "https://101inter:test101@stage.next.piter-online.net/providers/wifire/rates/internet-i-mobilnaya-svyaz",
            # "https://101inter:test101@stage.next.piter-online.net/providers/dom-ru/rates/nedorogoj-domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates/nedorogoj-domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/tele-2/rates/nedorogoj-domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/mts/rates/nedorogoj-domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/megafon/rates/nedorogoj-domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/beeline/rates/nedorogoj-domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/providers/wifire/rates/nedorogoj-domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/rates",
            # "https://101inter:test101@stage.next.piter-online.net/rates/domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/rates/internet-i-tv",
            # "https://101inter:test101@stage.next.piter-online.net/rates/internet-tv-mobile",
            # "https://101inter:test101@stage.next.piter-online.net/rates/internet-i-mobilnaya-svyaz",
            # "https://101inter:test101@stage.next.piter-online.net/rates/nedorogoj-domashnij-internet",
            # "https://101inter:test101@stage.next.piter-online.net/rates/internet-100-mbit",
            # "https://101inter:test101@stage.next.piter-online.net/rates/internet-300-mbit",
            # "https://101inter:test101@stage.next.piter-online.net/rates/internet-500-mbit",
            # "https://101inter:test101@stage.next.piter-online.net/orders/office",
            # "https://101inter:test101@stage.next.piter-online.net/orders/sat",
            # "https://101inter:test101@stage.next.piter-online.net/about/partners",
            # "https://101inter:test101@stage.next.piter-online.net/about/company",
            # "https://101inter:test101@stage.next.piter-online.net/about/contacts",
            # "https://101inter:test101@stage.next.piter-online.net/about/oplata-i-garantii"
        ]

        names = [
            "Главная",
            "Поиск по адресу",
            "Карта покрытия",
            "Районы",
            "Улицы",
            "Золотой дом",
            "Обычный дом",
            "Все районы",
            "Рейтинг",
            "Отзывы в регионе",
            "Отзывы провайдера",
            "Страница оставления отзыва",
            "Каталог",
            "Страница провайдера Домру",
            "Страница провайдера Ростелеком",
            "Страница провайдера Теле2",
            "Страница провайдера МТС",
            "Страница провайдера Мегафон",
            "Страница провайдера Билайн",
            "Страница провайдера Вип пров",
            "Страница провайдера Невип пров",
            "Тарифы провайдера (тег Все) Домру",
            "Тарифы провайдера (тег Все) Ростелеком",
            "Тарифы провайдера (тег Все) Теле2",
            "Тарифы провайдера (тег Все) МТС",
            "Тарифы провайдера (тег Все) Мегафон",
            "Тарифы провайдера (тег Все) Билайн",
            "Тарифы провайдера (тег Все) Вип пров",
            "Тарифы провайдера, тег Домашний интернет Домру",
            "Тарифы провайдера, тег Домашний интернет Ростелеком",
            "Тарифы провайдера, тег Домашний интернет Теле2",
            "Тарифы провайдера, тег Домашний интернет МТС",
            "Тарифы провайдера, тег Домашний интернет Мегафон",
            "Тарифы провайдера, тег Домашний интернет Билайн",
            "Тарифы провайдера, тег Домашний интернет Вип пров",
            "Тарифы провайдера, тег Интернет + ТВ Домру",
            "Тарифы провайдера, тег Интернет + ТВ Ростелеком",
            "Тарифы провайдера, тег Интернет + ТВ Билайн",
            "Тарифы провайдера, тег Интернет + ТВ Вип пров",
            "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь Ростелеком",
            "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь Теле2",
            "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь МТС",
            "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь Мегафон",
            "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь Билайн",
            "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь Вип пров",
            "Тарифы провайдера, тег Интернет + Мобильная связь Ростелеком",
            "Тарифы провайдера, тег Интернет + Мобильная связь Теле2",
            "Тарифы провайдера, тег Интернет + Мобильная связь МТС",
            "Тарифы провайдера, тег Интернет + Мобильная связь Мегафон",
            "Тарифы провайдера, тег Интернет + Мобильная связь Вип пров",
            "Тарифы провайдера, тег Акции Домру",
            "Тарифы провайдера, тег Акции Ростелеком",
            "Тарифы провайдера, тег Акции Теле2",
            "Тарифы провайдера, тег Акции МТС",
            "Тарифы провайдера, тег Акции Мегафон",
            "Тарифы провайдера, тег Акции Билайн",
            "Тарифы провайдера, тег Акции Вип пров",
            "Тарифы в регионе",
            "Тарифы в регионе, тег Домашний интернет",
            "Тарифы в регионе, тег Интернет + ТВ",
            "Тарифы в регионе, тег Интернет+ТВ+Мобильная связь",
            "Тарифы в регионе, тег Интернет + Мобильная связь",
            "Тарифы в регионе, тег Акции",
            "Тарифы в регионе, тег 100 Мб/с",
            "Тарифы в регионе, тег 300 Мб/с",
            "Тарифы в регионе, тег 500 Мб/с",
            "В офис",
            "На дачу",
            "Сотрудничество",
            "О нас",
            "Контакты",
            "Оплата и гарантии",

        ]

        for screen, name in zip(urls, names):
            try:
                uuid4 = uuid.uuid4()
                tags = TestsSeoCheck(driver, screen)
                tags.click_if_exists_first_seo()
                driver.get(screen)
                time.sleep(2)
                driver.execute_cdp_cmd('Page.enable', {})
                driver.execute_cdp_cmd('Page.setDeviceMetricsOverride', {
                    'width': 1920,
                    'height': 6000,
                    'deviceScaleFactor': 1,
                    'mobile': False,
                    'fitWindow': False
                })

                time.sleep(1)
                screenshot_path = f'C:/Users/Katerina/Desktop/screens/{name}.png'
                driver.save_screenshot(screenshot_path)
                print(f"Скриншот сохранен: {screenshot_path}")

            except Exception as e:
                print(f"Ошибка при работе с {screen}: {e}")

    class TestSearChrome:
        def test_check_search_chrome(self, driver):
            if HEADLESS:
                driver.set_window_size(1920, 1080)
            else:
                driver.maximize_window()

            urls = [
                "https://101inter:test101@stage.next.piter-online.net",
                "https://101inter:test101@stage.next.piter-online.net/orders/tohome",
                "https://101inter:test101@stage.next.piter-online.net/address",
                "https://101inter:test101@stage.next.piter-online.net/address/%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D1%81%D0%BA-id1250",
                "https://101inter:test101@stage.next.piter-online.net/address/%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D1%81%D0%BA-id1250/%D1%83%D0%BB-2-%D1%8F-%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%84%D0%BB%D0%BE%D1%82%D1%81%D0%BA%D0%B0%D1%8F-id295159",
                "https://101inter:test101@stage.next.piter-online.net/dom/ul-2-yakrasnoflotskaya-d-6-k2a-id1018691",
                "https://101inter:test101@stage.next.piter-online.net/leningradskaya-oblast/doma-nzl?house_id=4270758",
                "https://101inter:test101@stage.next.piter-online.net/all-districts",
                "https://101inter:test101@stage.next.piter-online.net/rating",
                "https://101inter:test101@stage.next.piter-online.net/reviews",
                "https://101inter:test101@stage.next.piter-online.net/rating/mts",
                "https://101inter:test101@stage.next.piter-online.net/feedback",
                "https://101inter:test101@stage.next.piter-online.net/providers",
                "https://101inter:test101@stage.next.piter-online.net/providers/dom-ru",
                "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom",
                "https://101inter:test101@stage.next.piter-online.net/providers/tele-2",
                "https://101inter:test101@stage.next.piter-online.net/providers/mts",
                "https://101inter:test101@stage.next.piter-online.net/providers/megafon",
                "https://101inter:test101@stage.next.piter-online.net/providers/beeline",
                "https://101inter:test101@stage.next.piter-online.net/providers/akado-neva",
                "https://101inter:test101@stage.next.piter-online.net/providers/awanti",
                "https://101inter:test101@stage.next.piter-online.net/providers/dom-ru/rates",
                "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates",
                "https://101inter:test101@stage.next.piter-online.net/providers/tele-2/rates",
                "https://101inter:test101@stage.next.piter-online.net/providers/mts/rates",
                "https://101inter:test101@stage.next.piter-online.net/providers/megafon/rates",
                "https://101inter:test101@stage.next.piter-online.net/providers/beeline/rates",
                "https://101inter:test101@stage.next.piter-online.net/providers/akado-neva/rates",
                "https://101inter:test101@stage.next.piter-online.net/providers/dom-ru/rates/domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates/domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/tele-2/rates/domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/mts/rates/domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/megafon/rates/domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/beeline/rates/domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/akado-neva/rates/domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/dom-ru/rates/internet-i-tv",
                "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates/internet-i-tv",
                "https://101inter:test101@stage.next.piter-online.net/providers/beeline/rates/internet-i-tv",
                "https://101inter:test101@stage.next.piter-online.net/providers/akado-neva/rates/internet-i-tv",
                "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates/internet-tv-mobile",
                "https://101inter:test101@stage.next.piter-online.net/providers/tele-2/rates/internet-tv-mobile",
                "https://101inter:test101@stage.next.piter-online.net/providers/mts/rates/internet-tv-mobile",
                "https://101inter:test101@stage.next.piter-online.net/providers/megafon/rates/internet-tv-mobile",
                "https://101inter:test101@stage.next.piter-online.net/providers/beeline/rates/internet-tv-mobile",
                "https://101inter:test101@stage.next.piter-online.net/providers/wifire/rates/internet-tv-mobile",
                "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates/internet-i-mobilnaya-svyaz",
                "https://101inter:test101@stage.next.piter-online.net/providers/tele-2/rates/internet-i-mobilnaya-svyaz",
                "https://101inter:test101@stage.next.piter-online.net/providers/mts/rates/internet-i-mobilnaya-svyaz",
                "https://101inter:test101@stage.next.piter-online.net/providers/megafon/rates/internet-i-mobilnaya-svyaz",
                "https://101inter:test101@stage.next.piter-online.net/providers/wifire/rates/internet-i-mobilnaya-svyaz",
                "https://101inter:test101@stage.next.piter-online.net/providers/dom-ru/rates/nedorogoj-domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/rostelecom/rates/nedorogoj-domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/tele-2/rates/nedorogoj-domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/mts/rates/nedorogoj-domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/megafon/rates/nedorogoj-domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/beeline/rates/nedorogoj-domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/providers/wifire/rates/nedorogoj-domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/rates",
                "https://101inter:test101@stage.next.piter-online.net/rates/domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/rates/internet-i-tv",
                "https://101inter:test101@stage.next.piter-online.net/rates/internet-tv-mobile",
                "https://101inter:test101@stage.next.piter-online.net/rates/internet-i-mobilnaya-svyaz",
                "https://101inter:test101@stage.next.piter-online.net/rates/nedorogoj-domashnij-internet",
                "https://101inter:test101@stage.next.piter-online.net/rates/internet-100-mbit",
                "https://101inter:test101@stage.next.piter-online.net/rates/internet-300-mbit",
                "https://101inter:test101@stage.next.piter-online.net/rates/internet-500-mbit",
                "https://101inter:test101@stage.next.piter-online.net/orders/office",
                "https://101inter:test101@stage.next.piter-online.net/orders/sat",
                "https://101inter:test101@stage.next.piter-online.net/about/partners",
                "https://101inter:test101@stage.next.piter-online.net/about/company",
                "https://101inter:test101@stage.next.piter-online.net/about/contacts",
                "https://101inter:test101@stage.next.piter-online.net/about/oplata-i-garantii"
            ]
            names = [
                "Главная",
                "Поиск по адресу",
                "Карта покрытия",
                "Районы",
                "Улицы",
                "Золотой дом",
                "Обычный дом",
                "Все районы",
                "Рейтинг",
                "Отзывы в регионе",
                "Отзывы провайдера",
                "Страница оставления отзыва",
                "Каталог",
                "Страница провайдера Домру",
                "Страница провайдера Ростелеком",
                "Страница провайдера Теле2",
                "Страница провайдера МТС",
                "Страница провайдера Мегафон",
                "Страница провайдера Билайн",
                "Страница провайдера Вип пров",
                "Страница провайдера Невип пров",
                "Тарифы провайдера (тег Все) Домру",
                "Тарифы провайдера (тег Все) Ростелеком",
                "Тарифы провайдера (тег Все) Теле2",
                "Тарифы провайдера (тег Все) МТС",
                "Тарифы провайдера (тег Все) Мегафон",
                "Тарифы провайдера (тег Все) Билайн",
                "Тарифы провайдера (тег Все) Вип пров",
                "Тарифы провайдера, тег Домашний интернет Домру",
                "Тарифы провайдера, тег Домашний интернет Ростелеком",
                "Тарифы провайдера, тег Домашний интернет Теле2",
                "Тарифы провайдера, тег Домашний интернет МТС",
                "Тарифы провайдера, тег Домашний интернет Мегафон",
                "Тарифы провайдера, тег Домашний интернет Билайн",
                "Тарифы провайдера, тег Домашний интернет Вип пров",
                "Тарифы провайдера, тег Интернет + ТВ Домру",
                "Тарифы провайдера, тег Интернет + ТВ Ростелеком",
                "Тарифы провайдера, тег Интернет + ТВ Билайн",
                "Тарифы провайдера, тег Интернет + ТВ Вип пров",
                "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь Ростелеком",
                "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь Теле2",
                "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь МТС",
                "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь Мегафон",
                "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь Билайн",
                "Тарифы провайдера, тег Интернет + ТВ+ мобильная связь Вип пров",
                "Тарифы провайдера, тег Интернет + Мобильная связь Ростелеком",
                "Тарифы провайдера, тег Интернет + Мобильная связь Теле2",
                "Тарифы провайдера, тег Интернет + Мобильная связь МТС",
                "Тарифы провайдера, тег Интернет + Мобильная связь Мегафон",
                "Тарифы провайдера, тег Интернет + Мобильная связь Вип пров",
                "Тарифы провайдера, тег Акции Домру",
                "Тарифы провайдера, тег Акции Ростелеком",
                "Тарифы провайдера, тег Акции Теле2",
                "Тарифы провайдера, тег Акции МТС",
                "Тарифы провайдера, тег Акции Мегафон",
                "Тарифы провайдера, тег Акции Билайн",
                "Тарифы провайдера, тег Акции Вип пров",
                "Тарифы в регионе",
                "Тарифы в регионе, тег Домашний интернет",
                "Тарифы в регионе, тег Интернет + ТВ",
                "Тарифы в регионе, тег Интернет+ТВ+Мобильная связь",
                "Тарифы в регионе, тег Интернет + Мобильная связь",
                "Тарифы в регионе, тег Акции",
                "Тарифы в регионе, тег 100 Мб/с",
                "Тарифы в регионе, тег 300 Мб/с",
                "Тарифы в регионе, тег 500 Мб/с",
                "В офис",
                "На дачу",
                "Сотрудничество",
                "О нас",
                "Контакты",
                "Оплата и гарантии",
            ]

            for screen, name in zip(urls, names):
                uuid4 = uuid.uuid4()
                tags = TestsSeoCheck(driver, screen)

                # Open the page (If tags.open() does not call driver.get(screen), remove this)
                tags.open()
                time.sleep(5)  # Consider using WebDriverWait instead
                # tags.scroll()
                # tags.click_if_exists_first_seo()
                # tags.click_if_exists_first_seo()
                # tags.scroll_second()
                # tags.click_if_exists_second_seo()
                tags.scroll_third()
                tags.click_if_exists_third_seo(0)
                tags.click_if_exists_third_seo(1)
                tags.click_if_exists_third_seo(2)
                tags.click_if_exists_third_seo(3)
                tags.click_if_exists_third_seo(4)
                tags.scroll_four()
                tags.click_if_exists_third_seo(5)
                tags.click_if_exists_third_seo(6)
                tags.scroll_five()
                tags.click_if_exists_third_seo(7)
                tags.click_if_exists_third_seo(8)
                tags.click_if_exists_third_seo(9)
                tags.click_if_exists_third_seo(10)

                # No need to reload the page, we can take a screenshot of the current state
                driver.execute_cdp_cmd('Page.enable', {})
                driver.execute_cdp_cmd('Page.setDeviceMetricsOverride', {
                    'width': 1920,
                    'height': 6000,
                    'deviceScaleFactor': 1,
                    'mobile': False,
                    'fitWindow': False
                })
                time.sleep(1)

                screenshot_path = f'C:/Users/Katerina/Desktop/screens/{name}.png'
                driver.save_screenshot(screenshot_path)
                print(f"Скриншот сохранен: {screenshot_path}")

            # except Exception as e:
            #     print(f"Ошибка при работе с {screen}: {e}")
