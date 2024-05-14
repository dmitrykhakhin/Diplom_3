import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_on_profile_link_button(self):
        self.click_on_element(HeaderLocators.PROFILE_LINK_BUTTON)

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_on_constructor_link_button(self):
        self.click_on_element(HeaderLocators.CONSTRUCTOR_LINK_BUTTON)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_on_order_feed_link_button(self):
        self.click_on_element(HeaderLocators.ORDER_FEED_BUTTON)
