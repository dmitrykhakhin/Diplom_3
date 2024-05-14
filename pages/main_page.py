import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажать на кнопку "Войти в аккаунт"')
    def click_on_login_to_account_button(self):
        self.click_on_element(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)

    @allure.step('Проверить наличие заголовка "Соберите бургер"')
    def should_be_constructor_heading(self):
        return self.get_text_from_element(MainPageLocators.CONSTRUCTOR_HEADING)

    @allure.step('Нажать на ингредиент в конструкторе')
    def click_on_ingredient(self):
        return self.click_on_element(MainPageLocators.FLUORESCENT_BUN)

    @allure.step('Проверить состояние окна "Детали ингредиента"')
    def check_ingredient_window_openness_condition(self):
        return self.get_value_from_element_attribute(MainPageLocators.INGREDIENT_DETAILS_WINDOW, "class")

    @allure.step('Закрыть окно "Детали ингредиента" кликом на крестик')
    def click_on_x_to_close_ingredient_window(self):
        self.click_on_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    @allure.step('Перейти к заданному разделу в конструкторе')
    def transit_to_ingredient_section(self, section_name):
        section_locator = self.format_locator(MainPageLocators.INGREDIENT_SECTION, section_name)
        self.click_on_element(section_locator)

    @allure.step('Перетащить ингредиент в корзину заказа')
    def drag_ingredient_on_order_basket(self, ingredient):
        ingredient_locator = self.format_locator(MainPageLocators.INGREDIENT_IN_CONSTRUCTOR, ingredient)
        self.drag_and_drop_element(ingredient_locator, MainPageLocators.ORDER_BASKET)

    @allure.step('Проверить значение счетчика')
    def check_ingredient_counter(self, ingredient):
        counter_locator = self.format_locator(MainPageLocators.INGREDIENT_COUNTER, ingredient)
        return self.get_text_from_element(counter_locator)

    @allure.step('Нажать "Оформить заказ"')
    def click_create_order(self):
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Проверить, что в модальном окне с информацией о созданном заказе'
                 ' есть строка "Ваш заказ начали готовить"')
    def should_be_text_in_created_order_info_window(self):
        return self.get_text_from_element(MainPageLocators.TEXT_FROM_CREATED_ORDER_INFO_MODAL_WINDOW)

    @allure.step('Закрыть окно с идентификатором созданного заказа кликом на крестик')
    def click_on_x_to_close_order_window(self):
        self.click_on_element(MainPageLocators.ORDER_WINDOW_CLOSE_BUTTON)

    @allure.step('Получить номер заказа в модальном окне с идентификатором созданного заказа')
    def get_order_number_from_order_window(self):
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER_IN_ORDER_WINDOW)
