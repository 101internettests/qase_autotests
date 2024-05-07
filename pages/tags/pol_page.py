import time
import allure
from locators.tags.pol_locators import Tagpagelocators, SpareTagsLocators, PopupFillTheAddress, PopupSuccess
from pages.base_page import BasePage


class OneHundredMainPage(BasePage):

    @allure.step("Выполнить проверку всех тегов страницы")
    def send_application_region_tag(self):
        with allure.step("Проверка TAG_INTERNET_AND_MOBILE"):
            self.element_is_visible(Tagpagelocators.TAG_INTERNET_AND_MOBILE).click()
            self.execute_actions_after_rates_click()
            self.choose_connection_type()
            self.voronezh_assert_text()
            time.sleep(60)
        # with allure.step("Проверка TAG_INTERNET_TV_MOBILE"):
        #     self.element_is_visible(Tagpagelocators.TAG_INTERNET_TV_MOBILE).click()
        #     self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        #     self.choose_connection_type()
        #     self.voronezh_assert_text()
        #     time.sleep(60)
        tags_to_check = [
            # Tagpagelocators.TAG_HOME_INTERNET,
            # Tagpagelocators.TAG_INTERNET_TV,
            # Tagpagelocators.TAG_CHEAP_INTERNET,
            # Tagpagelocators.TAG_100_MB,
            Tagpagelocators.TAG_300_MB,
            Tagpagelocators.TAG_500_MB,
            Tagpagelocators.TAG_ONLINE_CINEMA
        ]

        for tag in tags_to_check:
            with allure.step(f"Проверка {tag}"):
                self.element_is_visible(tag).click()
                self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS_SECOND).click()
                self.choose_connection_type()
                self.voronezh_assert_text()
                time.sleep(60)

    @allure.step("Заполнить адрес для города Санкт-Петербург")
    def execute_actions_after_rates_click(self):
        self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_FILLED_THE_STREET).send_keys('Димитрова ул')
        self.element_is_visible(PopupFillTheAddress.CLICK_ON_THE_STREET).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_FILLED_THE_HOUSE).send_keys('2')
        self.element_is_visible(PopupFillTheAddress.CLICK_ON_THE_HOUSE).click()

    @allure.step("Заполнить попап и выбрать тип соединения")
    def choose_connection_type(self):
        self.element_is_visible(PopupFillTheAddress.POP_UP_CONNECTION_TYPE).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_SELECT_CONNECTION_TYPE).click()
        self.element_is_visible(PopupFillTheAddress.POP_UP_BUTTON_CHECK).click()

    @allure.step("Проверить текст попапа и отправить заявку для города Санкт-Петербург")
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

    @allure.step("Заполнить адрес для города Санкт-Петербург")
    def send_application_provider(self):
        self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        self.element_is_visible(SpareTagsLocators.POP_UP_FILLED_THE_STREET).send_keys('Димитрова ул')
        self.element_is_visible(SpareTagsLocators.CLICK_ON_THE_STREET).click()
        self.element_is_visible(SpareTagsLocators.POP_UP_FILLED_THE_HOUSE).send_keys('2')
        self.element_is_visible(SpareTagsLocators.CLICK_ON_THE_HOUSE).click()

    @allure.step("Проверить текст попапа и отправить заявку для города Санкт-Петербург")
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
    def megafon_fill_the_address(self):
        with allure.step("Проверка TAG_INTERNET_TV_MOBILE"):
            self.send_application_provider()
            self.choose_connection_type()
            self.moscow_assert_text()
            time.sleep(60)
        # with allure.step("Проверка TAG_INTERNET_TV_MOBILE"):
        #     self.element_is_visible(Tagpagelocators.TAG_INTERNET_TV_MOBILE).click()
        #     self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS).click()
        #     self.choose_connection_type()
        #     self.moscow_assert_text()
        #     time.sleep(60)
        new_new_tags = [Tagpagelocators.TAG_HOME_INTERNET,
                        Tagpagelocators.TAG_INTERNET_TV]
                        # Tagpagelocators.TAG_CHEAP_INTERNET]
        for new_tag in new_new_tags:
            with allure.step(f"Проверка {new_tag}"):
                self.element_is_visible(new_tag).click()
                self.element_is_visible(PopupFillTheAddress.BUTTON_CHECK_THE_ADDRESS_SECOND).click()
                self.choose_connection_type()
                self.moscow_assert_text()
                time.sleep(60)
