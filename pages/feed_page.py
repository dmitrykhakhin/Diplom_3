import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Проверить наличие заголовка "Лента заказов"')
    def should_be_order_feed_heading(self):
        return self.get_text_from_element(FeedPageLocators.ORDER_FEED_HEADING)

    @allure.step('Нажать на первый заказ в ленте заказов')
    def click_on_first_order_in_order_feed_list(self):
        self.click_on_element(FeedPageLocators.FIRST_ORDER_IN_ORDER_FEED_LIST)

    @allure.step('Проверить, что окно с информацией о заказе открыто')
    def check_order_details_window_openness_condition(self):
        return self.get_value_from_element_attribute(FeedPageLocators.ORDER_DETAILS_WINDOW, "class")

    @allure.step('Проверить что заказ пользователя отображается в ленте заказов')
    def check_visibility_of_user_order_in_order_feed(self, order_number):
        order_item_locator = self.format_locator(FeedPageLocators.ORDER_NUMBER_IN_ORDER_FEED, order_number)
        return self.check_element_is_visible(order_item_locator)

    @allure.step('Проверить значение счетчика "Выполнено за всё время"')
    def check_completed_for_all_time_counter_value(self):
        return self.get_text_from_element(FeedPageLocators.COMPLETED_FOR_ALL_TIME_COUNTER)

    @allure.step('Проверить значение счетчика "Выполнено за сегодня"')
    def check_completed_today_counter_value(self):
        return self.get_text_from_element(FeedPageLocators.COMPLETED_TODAY_COUNTER)

    @allure.step('Проверить наличие номера заказа в разделе "В работе"')
    def check_visibility_of_order_number_in_work(self, order_number):
        order_number_locator = self.format_locator(FeedPageLocators.ORDER_NUMBER_IN_WORK, order_number)
        return self.check_element_is_visible(order_number_locator)
