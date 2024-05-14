import allure

from locators.forgot_password_page_locators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step('Проверить наличие заголовка "Восстановление пароля"')
    def should_be_recovery_password_page_heading(self):
        return self.get_text_from_element(ForgotPasswordLocators.RECOVERY_PASSWORD_HEADING)

    @allure.step('Проверить наличие поля для ввода email')
    def should_be_email_field(self):
        return self.get_text_from_element(ForgotPasswordLocators.EMAIL_FIELD_PLACEHOLDER)

    @allure.step('Заполнить поле "email"')
    def fill_email_field(self, email):
        self.add_text_to_element(ForgotPasswordLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Нажать кнопку "Восстановить"')
    def click_recovery_button(self):
        self.click_on_element(ForgotPasswordLocators.RECOVERY_BUTTON)
