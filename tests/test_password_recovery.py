import allure

from helper import Helper
from pages.forgot_password_page import ForgotPasswordPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля из главной страницы')
    @allure.description('Из главной страницы по клику на кнопку "Войти" делаем переход на страницу логина, \n'
                        'затем по клику на кнопку "Восстановить пароль" переходим на страницу восстановления пароля с '
                        'полем вода email')
    def test_transition_to_password_recovery_page_via_login_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.click_on_password_recovery_link()
        forgot_password_page = ForgotPasswordPage(driver)
        heading_text_on_page = forgot_password_page.should_be_recovery_password_page_heading()
        email_field_placeholder = forgot_password_page.should_be_email_field()
        assert heading_text_on_page == 'Восстановление пароля' and email_field_placeholder == 'Email'

    @allure.title('Переход на страницу восстановления пароля из хедера')
    @allure.description('По клику в хедере на кнопку "Личный Кабинет" делаем переход на страницу логина, \n'
                        'затем по клику на кнопку "Восстановить пароль" переходим на страницу восстановления пароля c '
                        'полем ввода email')
    def test_transition_to_password_recovery_page_via_profile_link_in_header(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_on_profile_link_button()
        login_page = LoginPage(driver)
        login_page.click_on_password_recovery_link()
        forgot_password_page = ForgotPasswordPage(driver)
        heading_text_on_page = forgot_password_page.should_be_recovery_password_page_heading()
        email_field_placeholder = forgot_password_page.should_be_email_field()
        assert heading_text_on_page == 'Восстановление пароля' and email_field_placeholder == 'Email'

    @allure.title('Ввод почты и клик по кнопке «Восстановить» на странице восстановления пароля')
    @allure.description('После ввода почты и клика по кнопке «Восстановить» на странице восстановления пароля, \n'
                        'переходим на страницу восстановления пароля с формой ввода пароля и кода из письма')
    def test_enter_email_and_click_recovery(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.click_on_password_recovery_link()
        forgot_password_page = ForgotPasswordPage(driver)
        random_email = Helper.generate_random_email()
        forgot_password_page.fill_email_field(random_email)
        forgot_password_page.click_recovery_button()
        reset_password_page = ResetPasswordPage(driver)
        heading_text_on_page = reset_password_page.should_be_reset_page_heading()
        password_field_placeholder = reset_password_page.should_be_password_field()
        code_field_placeholder = reset_password_page.should_be_code_field()
        assert (heading_text_on_page == 'Восстановление пароля' and
                password_field_placeholder == 'Пароль' and
                code_field_placeholder == 'Введите код из письма')

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным и подсвечивает его')
    @allure.description('На странице восстановления пароля, при нажатии на кнопку показать/скрыть пароль \n'
                        'поле "Пароль" становится активным и подсвечивается')
    def test_click_on_show_password_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.click_on_password_recovery_link()
        forgot_password_page = ForgotPasswordPage(driver)
        random_email = Helper.generate_random_email()
        forgot_password_page.fill_email_field(random_email)
        forgot_password_page.click_recovery_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.click_on_show_hide_button()
        class_attribute_value_from_password_field = reset_password_page.check_password_field_is_active()

        assert 'input_status_active' in class_attribute_value_from_password_field

