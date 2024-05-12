import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Нажать на ссылку "Восстановить пароль"')
    def click_on_password_recovery_link(self):
        self.click_on_element(LoginPageLocators.PASSWORD_RECOVERY_LINK)

    @allure.step('Ввести email')
    def fill_email_input_field(self, email):
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Ввести пароль')
    def fill_password_input_field(self, password):
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step('Нажать кнопку "Войти"')
    def click_login_button(self):
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Проверить наличие заголовка "Вход"')
    def should_be_login_page_heading(self):
        return self.get_text_from_element(LoginPageLocators.LOGIN_PAGE_HEADING)
