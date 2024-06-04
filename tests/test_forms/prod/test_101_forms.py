import allure
import time
from pages.forms.internet_page import FormsPage
from qaseio.pytest import qase


class TestInternetForms:
    @allure.title("Проверка формы 'жду звонка'")
    @qase.title("Проверка формы 'жду звонка' 101")
    @qase.id(356)
    def test_wait_call_form(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_on_msk()
        forms_page.chose_providers_burger_button()
        forms_page.fill_form_best_tariff()
        time.sleep(60)

    @allure.title("Проверка офисной заявки")
    @qase.title("Проверка офисной заявки 101")
    @qase.id(357)
    def test_office_form(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_on_msk()
        forms_page.fill_office_tender()
        forms_page.fill_office_tender_address()
        forms_page.fill_the_application()
        time.sleep(60)

    @allure.title("Проверка попапа номера телефона")
    @qase.title("Проверка попапа номера телефона 101")
    @qase.id(358)
    def test_popup_number(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.fill_address_on_main_page()
        forms_page.fill_popup_number()
        time.sleep(60)

    @allure.title("Проверка формы заявки 'адрес-тариф'")
    @qase.title("Проверка формы заявки 'адрес-тариф' 101")
    @qase.id(359)
    def test_tariff_form(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.fill_address_on_main_page()
        forms_page.close_popup()
        forms_page.fill_connect_to_application()
        time.sleep(60)

    @allure.title("Проверка формы загородной заявки на 101")
    @qase.title("Проверка формы загородной заявки на 101")
    @qase.id(360)
    def test_out_of_town_application(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.chose_button_internet_outtown()
        forms_page.fill_connect_to_application_outtown()
        time.sleep(60)

    @allure.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы' партнер")
    @qase.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы' партнер 101")
    @qase.id(361)
    def test_check_button_connect(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.chose_button_find_by_address()
        forms_page.fill_address_in_addresspage_second()
        forms_page.fill_connect_to_application_second()
        time.sleep(60)

    @allure.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы' непартнер")
    @qase.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы' непартнер 101")
    @qase.id(362)
    def test_check_button_connect_unpartner(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.chose_tariffs_button()
        forms_page.chose_mosnet_provider()
        # forms_page.fill_the_address_provider_card()
        # time.sleep(2)
        # forms_page.fill_popup_number()
        time.sleep(60)

    @allure.title("Проверка реферальной ссылки с тарифа")
    @qase.title("Проверка реферальной ссылки с тарифа 101")
    @qase.id(363)
    def test_check_url_provider(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.change_region_on_msk()
        forms_page.chose_tariffs_button()
        forms_page.chose_abk_provider()
        forms_page.check_redirect()
        target_url = 'https://avk-wellcom.ru/zayavka-na-podklyuchenie.html'
        assert driver.current_url == target_url

    @allure.title("Проверка формы 1 клик на главной странице")
    @qase.title("Проверка формы 1 клик на главной странице 101")
    @qase.id(364)
    def test_one_click_main(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/voronezh")
        forms_page.open()
        forms_page.scroll_to_form()
        forms_page.one_click_main()
        time.sleep(60)

    @allure.title("Проверка формы 1 клик на странице отзывов")
    @qase.title("Проверка формы 1 клик на странице отзывов 101")
    @qase.id(365)
    def test_one_click_review(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/chelyabinsk/reviews")
        forms_page.open()
        forms_page.one_click_review()
        time.sleep(60)

    @allure.title("Проверка формы 1 клик на странице поиска по адресу")
    @qase.title("Проверка формы 1 клик на странице поиска по адресу 101")
    @qase.id(366)
    def test_one_click_tohome(self, driver):
        forms_page = FormsPage(driver, "https://101internet.ru/chelyabinsk/orders/tohome")
        forms_page.open()
        forms_page.scroll_to_tohome()
        forms_page.one_click_main()
        time.sleep(60)