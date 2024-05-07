import allure
import time
from locators.forms.internet_locator import WaitCallLocators, OfficeOrder, AddreesTariffForm, OutOfTownApplication, OneClickLocators
from locators.forms.internet_locator import RecentlyConnectionTariffs, NonPartnerCardRecCon, ReferralUrlTariff, PopUpPhoneNub
from locators.forms.mol_locators import WaitMOLCallLocators, PopUpPhoneNubMsk, ReferralUrlTariffMOL, WriteTariffNameMOL
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class FormsPage(BasePage):
    @allure.step("Выбрать отзывы в футере")
    def chose_reviews_button(self):
        scroll = self.element_is_visible(WaitMOLCallLocators.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(WaitMOLCallLocators.REVIEWS).click()

    @allure.step("Ввести номер в форме 'Поможем выбрать лучший тариф'")
    def fill_form_best_tariff(self):
        scroll = self.element_is_visible(WaitCallLocators.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(WaitCallLocators.BUTTON_WAIT_FOR_CALL).click()
        self.element_is_visible(WaitCallLocators.WRITE_TELEPHONE_NUMBER).send_keys("1111111111")
        self.element_is_visible(WaitCallLocators.BUTTON_CALL_ME).click()

    @allure.step("Выбрать 'интернет в офис' в меню бургер")
    def fill_office_tender(self):
        self.element_is_visible(OfficeOrder.INTERNET_IN_OFFICE).click()

    @allure.step("Заполнить адрес")
    def fill_office_tender_address(self):
        self.element_is_visible(OfficeOrder.CHOOSE_STREET).send_keys("Тестовый б-р")
        self.element_is_visible(OfficeOrder.CLICK_ON_STREET).click()
        self.element_is_visible(OfficeOrder.CHOOSE_HOUSE).send_keys("1")
        self.element_is_visible(OfficeOrder.CLICK_ON_HOUSE).click()
        self.element_is_visible(OfficeOrder.TENDER_BUTTON).click()

    @allure.step("Заполнить заявку на подключение интернета в офис")
    def fill_the_application(self):
        self.element_is_visible(OfficeOrder.PERSON_INPUT).send_keys("Тест")
        self.element_is_visible(OfficeOrder.TELEPHON_INPUT).send_keys("1111111111")
        self.element_is_visible(OfficeOrder.BUTTON_SEND_ORDER).click()

    @allure.step("Выбрать регион Москва в хедере")
    def change_region_moscow(self):
        self.element_is_visible(WaitCallLocators.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(WaitCallLocators.WRITE_NAME_OF_REGION).send_keys("Москва")
        time.sleep(1)
        self.element_is_visible(PopUpPhoneNubMsk.CHOOSE_MOSCOW).click()

    @allure.step("Заполнить адрес на главной странице")
    def fill_address_on_main_page(self):
        self.element_is_visible(OfficeOrder.CHOOSE_STREET).send_keys("Шарикоподшипниковская")
        self.element_is_visible(OfficeOrder.CLICK_ON_STREET).click()
        self.element_is_visible(OfficeOrder.CHOOSE_HOUSE).send_keys("11")
        self.element_is_visible(OfficeOrder.CLICK_ON_HOUSE).click()
        self.element_is_visible(OfficeOrder.CHOOSE_TYPE).click()
        self.element_is_visible(PopUpPhoneNubMsk.BUTTOM_SHOW_TARIFFS).click()

    @allure.step("Открыть попап")
    def open_popup(self):
        self.element_is_visible(AddreesTariffForm.OPEN_PPOPUP).click()

    @allure.step("Ввести номер телефона в попап")
    def fill_popup_number(self):
        text_in_pop_up = self.element_is_present(PopUpPhoneNub.POP_UP_TEXT).text
        if text_in_pop_up == ("Отлично! Подключение возможно. Введите номер "
                              "телефона, оператор перезвонит вам в ближайшее "
                              "время."):
            self.element_is_visible(PopUpPhoneNub.NUMBER_SECOND_INPUT).send_keys('1111111111')
            self.element_is_visible(PopUpPhoneNub.BUTTON_SUBMIT_APPLICATION).click()
            print("Провайдер доступен в этом доме")
        elif text_in_pop_up != ("Отлично! Подключение возможно. Введите номер "
                                "телефона, оператор перезвонит вам в ближайшее "
                                "время."):
            self.element_is_visible(PopUpPhoneNub.NUMBER_INPUT).send_keys('1111111111')
            self.element_is_visible(PopUpPhoneNub.BUTTON_SHOW_RESULTS).click()
            print("Провайдер недоступен в этом доме, отправлена заявки на другие")

    @allure.step("Закрыть попап")
    def close_popup(self):
        if self.element_is_present(AddreesTariffForm.CLOSE_POP_UP):
            self.element_is_visible(AddreesTariffForm.CLOSE_POP_UP).click()

    @allure.step("Заполнить заявку по кнопке 'подключить'")
    def fill_connect_to_application(self):
        self.element_is_visible(AddreesTariffForm.BUTTON_CONNECT).click()
        time.sleep(2)
        self.write_tariff_name()
        if self.element_is_visible(AddreesTariffForm.INPUT_MOBILE_PHONE):
            self.element_is_visible(AddreesTariffForm.INPUT_MOBILE_PHONE).send_keys("1111111111")
            self.element_is_visible(AddreesTariffForm.BUTTON_SEND_APPLICATION).click()
        else:
            if self.element_is_visible(AddreesTariffForm.INPUT_NUMBER_SECOND):
                self.element_is_visible(AddreesTariffForm.INPUT_NUMBER_SECOND).send_keys("1111111111")
                self.element_is_visible(AddreesTariffForm.BUTTON_SEND_APL_SECOND).click()
            else:
                self.element_is_visible(AddreesTariffForm.TARIFF_POPUP_NUM).send_keys("1111111111")
                self.element_is_visible(AddreesTariffForm.BUTTON_SEND_APL_SECOND).click()

    @allure.step("Выбрать 'интернет на дачу' в футере")
    def chose_button_internet_outtown_mol(self):
        scroll = self.element_is_visible(WaitMOLCallLocators.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(OutOfTownApplication.OUT_OF_TOWN_BUTTON).click()

    @allure.step("Заполнить заявку в частном доме")
    def fill_connect_to_application_outtown(self):
        self.element_is_visible(OutOfTownApplication.INPUT_NAME).send_keys("Тест")
        self.element_is_visible(OutOfTownApplication.INPUT_NUMBER).send_keys("1111111111")
        self.element_is_visible(OutOfTownApplication.BUTTON_CONNECTION).click()
        success_text = self.element_is_visible(OutOfTownApplication.TEXT_ASSERT)
        assert success_text.text == "Спасибо, ваша заявка на подключение принята и уже отправлена в работу! Ждите звонка в ближайшее время!"

    @allure.step("Выбрать 'Поиск по адресу' внизу страницы")
    def chose_button_find_by_address(self):
        scroll = self.element_is_visible(WaitMOLCallLocators.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(RecentlyConnectionTariffs.BUTTON_FIND_ADDRESS).click()

    @allure.step("Заполнить адрес через кнопку 'проверить адрес' вариант 2")
    def fill_address_in_addresspage_second(self):
        self.element_is_visible(RecentlyConnectionTariffs.BUTTON_FOR_CONNECTION).click()
        time.sleep(3)

    @allure.step("Заполнить заявку по кнопке 'подключить' 2 варинт")
    def fill_connect_to_application_second(self):
        time.sleep(2)
        self.write_tariff_name()
        if self.element_is_visible(AddreesTariffForm.INPUT_MOBILE_PHONE):
            self.element_is_visible(AddreesTariffForm.INPUT_MOBILE_PHONE).send_keys("1111111111")
            self.element_is_visible(AddreesTariffForm.BUTTON_SEND_APPLICATION).click()
        else:
            if self.element_is_visible(AddreesTariffForm.INPUT_NUMBER_SECOND):
                self.element_is_visible(AddreesTariffForm.INPUT_NUMBER_SECOND).send_keys("1111111111")
                self.element_is_visible(AddreesTariffForm.BUTTON_SEND_APL_SECOND).click()
            else:
                self.element_is_visible(AddreesTariffForm.TARIFF_POPUP_NUM).send_keys("1111111111")
                self.element_is_visible(AddreesTariffForm.BUTTON_SEND_APL_SECOND).click()

    @allure.step("Заполнить адрес через кнопку 'проверить адрес'")
    def fill_address_in_addresspage(self):
        self.element_is_visible(RecentlyConnectionTariffs.BUTTON_CHECK_ADDRESS).click()
        self.element_is_visible(RecentlyConnectionTariffs.INPUT_STREET).send_keys("Тестовская")
        self.element_is_visible(RecentlyConnectionTariffs.CLICK_ON_THE_STREET).click()
        self.element_is_visible(RecentlyConnectionTariffs.INPUT_HOUSE).send_keys("1")
        self.element_is_visible(RecentlyConnectionTariffs.CLICK_ON_THE_HOUSE).click()
        self.element_is_visible(RecentlyConnectionTariffs.CHOOSE_TYPE_OF_CONNECTION).click()
        self.element_is_visible(RecentlyConnectionTariffs.CLICK_ON_TYPE_OF_CONNECTION).click()
        self.element_is_visible(RecentlyConnectionTariffs.CHECK_CONNECTION).click()

    @allure.step("Выбрать 'провайдеры' в меню бургер")
    def chose_providers_burger_button(self):
        self.element_is_visible(NonPartnerCardRecCon.PROVIDERS_BUTTON).click()
        time.sleep(3)

    @allure.step("Выбрать в фильтрах 'Моснет'")
    def chose_mosnet_provider(self):
        self.element_is_visible(NonPartnerCardRecCon.CHOSE_PROVIDER_FILTER).send_keys("Моснет")
        self.element_is_visible(NonPartnerCardRecCon.CHOSE_MOSNET).click()
        self.element_is_visible(NonPartnerCardRecCon.ACCEPT_FILTER).click()
        self.element_is_visible(NonPartnerCardRecCon.CLICK_ON_PIC_MOSNET).click()
        time.sleep(3)

    @allure.step("Заполнить адрес с карточке провайдера")
    def fill_the_address_provider_card(self):
        self.element_is_visible(NonPartnerCardRecCon.INPUT_STREET).send_keys("Тестовый")
        self.element_is_visible(NonPartnerCardRecCon.CLICK_ON_THE_STREET).click()
        self.element_is_visible(NonPartnerCardRecCon.INPUT_HOUSE).send_keys("1")
        self.element_is_visible(NonPartnerCardRecCon.CLICK_ON_THE_HOUSE).click()
        self.element_is_visible(NonPartnerCardRecCon.CHOOSE_TYPE).click()
        self.element_is_visible(NonPartnerCardRecCon.SHOW_TARIFFS).click()

    @allure.step("Выбрать регион Московская область в хедере")
    def change_region_moscow(self):
        self.element_is_visible(WaitCallLocators.CHOOSE_THE_REGION).click()
        time.sleep(3)
        self.element_is_visible(ReferralUrlTariffMOL.CHOSE_MOSCOW_REGION).click()
        time.sleep(3)

    @allure.step("Выбрать в фильтрах 'АВК-Веллком'")
    def chose_abk_provider(self):
        self.element_is_visible(NonPartnerCardRecCon.CHOSE_PROVIDER_FILTER).send_keys("АВК-Веллком")
        self.element_is_visible(ReferralUrlTariff.CHOSE_ABK_WELCOME).click()
        self.element_is_visible(NonPartnerCardRecCon.ACCEPT_FILTER).click()
        time.sleep(2)
        self.element_is_present(ReferralUrlTariff.CLICK_ON_PIC_AVK_WELCOME).click()
        time.sleep(3)

    @allure.step("Перейти на сайт провайдера по кнопке'подключить' у провайдера 'АВК-Веллком'")
    def check_redirect(self):
        scroll = self.element_is_visible(ReferralUrlTariff.SCROLL)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.element_is_visible(ReferralUrlTariff.CONNECT_BUTTON).click()
        self.switch_handles_window()

    @allure.step("Написать название тарифа в консоль")
    def write_tariff_name(self):
        if self.element_is_visible(WriteTariffNameMOL.NAME_OF_TARIFF):
            name_element = self.element_is_visible(WriteTariffNameMOL.NAME_OF_TARIFF)
            if name_element is not None:
                name_text = name_element.text
                print(name_text)
            else:
                print("Элемент не найден или не содержит текст")
        if self.element_is_visible(WriteTariffNameMOL.NAME_OF_TARIFF_STAND):
            name_element = self.element_is_visible(WriteTariffNameMOL.NAME_OF_TARIFF_STAND)
            if name_element is not None:
                name_text = name_element.text
                print(name_text)
            else:
                print("Элемент не найден или не содержит текст")
        if self.element_is_visible(WriteTariffNameMOL.NAME_OF_TARIFF_B):
            name_element = self.element_is_visible(WriteTariffNameMOL.NAME_OF_TARIFF_B)
            if name_element is not None:
                name_text = name_element.text
                print(name_text)
            else:
                print("Элемент не найден или не содержит текст")

    @allure.step("Скролл до формы 1 клик снизу страницы")
    def scroll_to_form(self):
        scroll = self.element_is_visible(OneClickLocators.SCROLL_MAIN_PAGE)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()

    @allure.step("Скролл до формы 1 клик на страринце поиска по адресу")
    def scroll_to_tohome(self):
        scroll = self.element_is_visible(OneClickLocators.SCROLL_TOHOME_PAGE)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()

    @allure.step("Заполнить форму 1 клик на главной странице")
    def one_click_main(self):
        self.element_is_visible(OneClickLocators.NUMBER_OF_PHONE).send_keys("1111111111")
        self.element_is_visible(OneClickLocators.BUTTON_CHOSE_THE_TARIFF).click()
        success = self.element_is_visible(OneClickLocators.TEXT_CHECK)
        assert success.text == "Ваша заявка принята! Мы свяжемся с вами в ближайшее время."

    @allure.step("Заполнить форму 1 клик на странице отзывов")
    def one_click_review(self):
        self.element_is_visible(OneClickLocators.NUMBER_OF_PHONE).send_keys("1111111111")
        self.element_is_visible(OneClickLocators.BUTTON_GET_CONSULTATION).click()
        success = self.element_is_visible(OneClickLocators.TEXT_CHECK)
        assert success.text == "Ваша заявка принята! Мы свяжемся с вами в ближайшее время."
