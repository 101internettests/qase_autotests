from pages.forms.mol_page import FormsPage
import allure
import time


class TestMOLForms:

    @allure.title("Проверка формы 'жду звонка'")
    def test_wait_call_mol_form(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/providers")
        forms_page.open()
        forms_page.fill_form_best_tariff()
        time.sleep(60)

    @allure.title("Проверка офисной заявки")
    def test_office_form(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms_page.open()
        forms_page.fill_office_tender()
        forms_page.fill_office_tender_address()
        forms_page.fill_the_application()
        time.sleep(60)

    @allure.title("Проверка попапа номера телефона")
    def test_popup_number_moscow(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.fill_address_on_main_page()
        forms_page.fill_popup_number()
        time.sleep(60)

    @allure.title("Проверка формы заявки 'адрес-тариф'")
    def test_tariff_form_moscow(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.fill_address_on_main_page()
        forms_page.close_popup()
        forms_page.fill_connect_to_application()
        time.sleep(60)

    @allure.title("Проверка формы загородной заявки на МОЛ")
    def test_out_of_town_application_moscow(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.chose_button_internet_outtown_mol()
        forms_page.fill_connect_to_application_outtown()
        time.sleep(60)

    # @allure.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы' партнер")
    # @qase.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы' партнер МОЛ")
    # @qase.id(372)
    # def test_check_button_connect_mol(self, driver):
    #     forms_page = FormsPage(driver, "https://www.moskvaonline.ru/")
    #     forms_page.open()
    #     forms_page.change_region_moscow()
    #     forms_page.chose_button_find_by_address()
    #     forms_page.fill_address_in_addresspage_second()
    #     forms_page.fill_connect_to_application_second()
        # forms_page.fill_address_in_addresspage()
        # time.sleep(2)
        # forms_page.fill_popup_number()
        # time.sleep(60)

    @allure.title("Проверка кнопки 'Подключить' в блоке 'Недавно подключённые тарифы' непартнер")
    def test_check_button_connect_unpartner_mol(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms_page.open()
        forms_page.change_region_moscow()
        forms_page.chose_tariffs_button()
        forms_page.chose_mosnet_provider()
        forms_page.fill_the_address_provider_card()
        time.sleep(2)
        forms_page.fill_popup_number()
        # time.sleep(60)

    # @allure.title("Проверка реферальной ссылки с тарифа")
    # @qase.title("Проверка реферальной ссылки с тарифа МОЛ")
    # @qase.id(374)
    # def test_check_url_provider_mol(self, driver):
    #     forms_page = FormsPage(driver, "https://www.moskvaonline.ru/")
    #     forms_page.open()
    #     forms_page.change_region_moscow()
    #     forms_page.chose_tariffs_button()
    #     forms_page.chose_abk_provider()
    #     forms_page.check_redirect()
    #     target_url = 'https://avk-wellcom.ru/zayavka-na-podklyuchenie.html'
    #     assert driver.current_url == target_url

    @allure.title("Проверка формы 1 клик на главной странице")
    def test_one_click_main(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/")
        forms_page.open()
        forms_page.scroll_to_form()
        forms_page.one_click_main()
        time.sleep(60)

    @allure.title("Проверка формы 1 клик на странице отзывов")
    def test_one_click_review(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/reviews")
        forms_page.open()
        forms_page.one_click_review()
        time.sleep(60)

    @allure.title("Проверка формы 1 клик на странице поиска по адресу")
    def test_one_click_tohome(self, driver):
        forms_page = FormsPage(driver, "https://www.moskvaonline.ru/orders/tohome")
        forms_page.open()
        forms_page.scroll_to_tohome()
        forms_page.one_click_main()
        time.sleep(60)

