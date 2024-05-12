import allure

from locators.reset_password_page_locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step('Проверить наличие заголовка "Восстановление пароля"')
    def should_be_reset_page_heading(self):
        return self.get_text_from_element(ResetPasswordLocators.RESET_PASSWORD_HEADING)

    @allure.step('Проверить наличие поля для ввода пароля')
    def should_be_password_field(self):
        return self.get_text_from_element(ResetPasswordLocators.PASSWORD_FIELD_PLACEHOLDER)

    @allure.step('Проверить наличие поля для ввода кода из письма')
    def should_be_code_field(self):
        return self.get_text_from_element(ResetPasswordLocators.CODE_FIELD_PLACEHOLDER)

    @allure.step('Нажать кнопку показать/скрыть пароль')
    def click_on_show_hide_button(self):
        self.click_on_element(ResetPasswordLocators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step('Проверить, что поле "Пароль" стало активным и подсвечено')
    def check_password_field_is_active(self):
        return self.get_value_from_element_attribute(ResetPasswordLocators.PASSWORD_INPUT_SECTION, "class")
