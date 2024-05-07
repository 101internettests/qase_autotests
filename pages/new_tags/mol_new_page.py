import time
import allure
from locators.tags.mol_locators import TagPagelocators, SpareTagsLocators, PopupFillTheAddress, PopupSuccess
from locators.tags.internet_locators import WriteTariffName, AddreesTariffForm
from pages.base_page import BasePage


class OneHundredMainPage(BasePage):

    @allure.step("Выполнить проверку всех тегов страницы")
    def send_application_region_tag(self):
        with allure.step("Проверка TAG_INTERNET_AND_MOBILE"):
            self.element_is_visible(TagPagelocators.TAG_INTERNET_AND_MOBILE).click()
            self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
            self.send_application_from_new_window_new()
            # self.driver.back()
            time.sleep(60)
        tags_to_check = [
            # TagPagelocators.TAG_HOME_INTERNET,
            TagPagelocators.TAG_INTERNET_TV,
            TagPagelocators.TAG_CHEAP_INTERNET,
            TagPagelocators.TAG_100_MB,
            # TagPagelocators.TAG_300_MB,
            # TagPagelocators.TAG_500_MB,
            # TagPagelocators.TAG_ONLINE_CINEMA
        ]

        for tag in tags_to_check:
            with allure.step(f"Проверка {tag}"):
                self.element_is_visible(tag).click()
                self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS_SECOND).click()
                self.send_application_from_new_window_new()
                # self.driver.back()
                time.sleep(60)

    @allure.step("Заполнить адрес для города Москва")
    def execute_actions_after_rates_click(self):
        self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_FILLED_THE_STREET).send_keys('Академика Зелинского ул')
        self.element_is_visible(PopupFillTheAddress.CLICK_ON_THE_STREET).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_FILLED_THE_HOUSE).send_keys('38к8')
        self.element_is_visible(PopupFillTheAddress.CLICK_ON_THE_HOUSE).click()

    @allure.step("Заполнить попап и выбрать тип соединения")
    def choose_connection_type(self):
        self.element_is_visible(PopupFillTheAddress.POP_UP_CONNECTION_TYPE).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_SELECT_CONNECTION_TYPE).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_BUTTON_CHECK).click()

    @allure.step("Проверить текст попапа и отправить заявку для города Москва")
    def voronezh_assert_text(self):
        text_in_pop_up = self.element_is_present(PopupSuccess.POP_UP_TEXT).text
        target_text = "Отлично! Подключение возможно. Введите номер телефона, оператор перезвонит вам в ближайшее время."
        if text_in_pop_up == target_text:
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_NUMBER).send_keys('1111111111')
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_BUTTON).click()
            self.element_is_visible(PopupSuccess.CLOSE_SUCCESS_WINDOW).click()
            print("Провайдер доступен в этом доме")
        elif text_in_pop_up != target_text:
            self.element_is_visible(PopupSuccess.POP_UP_NOT_SUCCESS_NUMBER).send_keys('1111111111')
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_BUTTON).click()
            self.element_is_visible(PopupSuccess.CLOSE_THE_WINDOW).click()
            self.driver.back()
            print("Провайдер недоступен в этом доме, отправлена заявки на другие")

    # для старого теста
    @allure.step("Заполнить адрес для города Москва")
    def send_application_provider(self):
        self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        self.element_is_visible(SpareTagsLocators.POP_UP_FILLED_THE_STREET).send_keys('Академика Зелинского ул')
        self.element_is_visible(SpareTagsLocators.CLICK_ON_THE_STREET).click()
        self.element_is_visible(SpareTagsLocators.POP_UP_FILLED_THE_HOUSE).send_keys('38к8')
        self.element_is_visible(SpareTagsLocators.CLICK_ON_THE_HOUSE).click()

    @allure.step("Выполнить проверку тегов страницы")
    def new_application_provider(self):
        self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        self.send_application_from_new_window()
        # self.driver.back()
        time.sleep(60)
        # with allure.step("Проверка TAG_INTERNET_TV_MOBILE"):
            # self.driver.back()
            # self.element_is_visible(TagPagelocators.TAG_INTERNET_TV_MOBILE).click()
            # self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
            # self.choose_connection_type()
            # self.moscow_assert_text()
            # time.sleep(60)
        new_new_tags = [
                        # TagPagelocators.TAG_HOME_INTERNET,
                        # TagPagelocators.TAG_INTERNET_TV]
                        TagPagelocators.TAG_CHEAP_INTERNET,
                        TagPagelocators.TAG_ONLINE_CINEMA]
        for new_tag in new_new_tags:
            with allure.step(f"Проверка {new_tag}"):
                self.element_is_visible(new_tag).click()
                self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS_SECOND).click()
                self.send_application_from_new_window()
                # self.driver.back()
                time.sleep(60)

    @allure.step("Проверить текст попапа и отправить заявку для города Москва")
    def moscow_assert_text(self):
        text_in_pop_up = self.element_is_present(PopupSuccess.POP_UP_TEXT).text
        if text_in_pop_up == ("Отлично! Подключение возможно. Введите номер "
                              "телефона, оператор перезвонит вам в ближайшее "
                              "время."):
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_NUMBER).send_keys('1111111111')
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_BUTTON).click()
            self.element_is_visible(PopupSuccess.CLOSE_SUCCESS_WINDOW).click()
            print("Провайдер доступен в этом доме")
        elif text_in_pop_up != ("Отлично! Подключение возможно. Введите номер "
                                "телефона, оператор перезвонит вам в ближайшее "
                                "время."):
            self.element_is_visible(SpareTagsLocators.POP_UP_NOT_SUCCESS_NUMBER).send_keys('1111111111')
            self.element_is_visible(PopupSuccess.POP_UP_SUCCESS_BUTTON).click()
            self.element_is_visible(SpareTagsLocators.CLOSE_THE_WINDOW).click()
            print("Провайдер недоступен в этом доме, отправлена заявки на другие")

    @allure.step("Выполнить проверку тегов страницы")
    def new_application_provider_ekb(self):
        self.send_application_provider()
        self.choose_connection_type()
        self.moscow_assert_text()
        time.sleep(60)
        with allure.step("Проверка TAG_INTERNET_TV_MOBILE"):
            self.element_is_visible(TagPagelocators.TAG_INTERNET_TV_MOBILE).click()
            self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
            self.choose_connection_type()
            self.moscow_assert_text()
            time.sleep(60)
        new_new_tags = [TagPagelocators.TAG_HOME_INTERNET,
                        TagPagelocators.TAG_INTERNET_TV,
                        TagPagelocators.TAG_CHEAP_INTERNET,
                        TagPagelocators.TAG_ONLINE_CINEMA]
        for new_tag in new_new_tags:
            with allure.step(f"Проверка {new_tag}"):
                self.element_is_visible(new_tag).click()
                self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS_SECOND).click()
                self.choose_connection_type()
                self.moscow_assert_text()
                time.sleep(60)

    @allure.step("Выполнить проверку тегов страницы")
    def megafon_fill_the_address(self):
        with allure.step("Проверка TAG_INTERNET_TV_MOBILE"):
            self.send_application_provider()
            self.choose_connection_type()
            self.moscow_assert_text()
            self.driver.back()
            time.sleep(60)
        new_new_tags = [TagPagelocators.TAG_HOME_INTERNET,
                        TagPagelocators.TAG_INTERNET_TV,
                        TagPagelocators.TAG_CHEAP_INTERNET]
        for new_tag in new_new_tags:
            with allure.step(f"Проверка {new_tag}"):
                self.element_is_visible(new_tag).click()
                self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS_SECOND).click()
                self.choose_connection_type()
                self.moscow_assert_text()
                self.driver.back()
                time.sleep(60)

    @allure.step("Отправить заявку")
    def send_application_from_new_window(self):
        # self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        # self.element_is_visible(AddreesTariffForm.BUTTON_CONNECT).click()
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
                self.element_is_visible(AddreesTariffForm.BUTTON_SEND_APL_THRID).click()
                self.element_is_visible(AddreesTariffForm.THANKYOU_BUTTON).click()

    @allure.step("Отправить заявку")
    def send_application_from_new_window_new(self):
        # self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        # self.element_is_visible(AddreesTariffForm.BUTTON_CONNECT).click()
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
                self.element_is_visible(AddreesTariffForm.THANKYOU_BUTTON).click()

    @allure.step("Написать название тарифа в консоль")
    def write_tariff_name(self):
        if self.element_is_visible(WriteTariffName.NAME_OF_TARIFF):
            name_element = self.element_is_visible(WriteTariffName.NAME_OF_TARIFF)
            if name_element is not None:
                name_text = name_element.text
                print(name_text)
            else:
                print("Элемент не найден или не содержит текст")
        if self.element_is_visible(WriteTariffName.NAME_OF_TARIFF_STAND):
            name_element = self.element_is_visible(WriteTariffName.NAME_OF_TARIFF_STAND)
            if name_element is not None:
                name_text = name_element.text
                print(name_text)
            else:
                print("Элемент не найден или не содержит текст")
        if self.element_is_visible(WriteTariffName.NAME_OF_TARIFF_B):
            name_element = self.element_is_visible(WriteTariffName.NAME_OF_TARIFF_B)
            if name_element is not None:
                name_text = name_element.text
                print(name_text)
            else:
                print("Элемент не найден или не содержит текст")