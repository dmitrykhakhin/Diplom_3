import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step('Проверить наличие текста "В этом разделе вы можете изменить свои персональные данные"')
    def should_be_information_paragraph(self):
        return self.get_text_from_element(ProfilePageLocators.INFORMATION_PARAGRAPH)

    @allure.step('Нажать на ссылку "История заказов"')
    def click_on_order_history_link(self):
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('Проверить, что ссылка стала "История заказов" стала активной')
    def check_order_history_link_is_active(self):
        return self.get_value_from_element_attribute(ProfilePageLocators.ORDER_HISTORY_LINK, "class")

    @allure.step('Проверить, что текущий url содержит путь "/account/order-history"')
    def should_be_order_history_path_in_current_url(self):
        return self.get_current_url()

    @allure.step('Проверить, что в Истории заказов отображается номер последнего заказа')
    def check_last_order_number(self):
        return self.get_text_from_element(ProfilePageLocators.NUMBER_OF_LAST_ORDER)

    @allure.step('Проверить название бургера в последнем заказе в Истории заказов')
    def check_burger_name_in_last_order(self):
        return self.get_text_from_element(ProfilePageLocators.BURGER_NAME_IN_LAST_ORDER)

    @allure.step('Нажать кнопку "Выйти"')
    def click_on_logout_button(self):
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)


