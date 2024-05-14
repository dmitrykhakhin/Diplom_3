import allure

from data import Burger
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfile:
    @allure.title('Переход по клику на "Личный кабинет"')
    @allure.description('Авторизуемся, затем нажимаем кнопку "Личный кабинет" в хэдере сайта. \n'
                        'На странице личного кабинета проверяем наличие текста "В этом разделе вы можете изменить '
                        'свои персональные данные"')
    def test_transition_to_profile(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_on_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_input_field(user["email"])
        login_page.fill_password_input_field(user["password"])
        login_page.click_login_button()
        header_page = HeaderPage(driver)
        header_page.click_on_profile_link_button()
        profile_page = ProfilePage(driver)
        text_from_paragraph = profile_page.should_be_information_paragraph()
        expected_text = 'В этом разделе вы можете изменить свои персональные данные'
        assert text_from_paragraph == expected_text

    @allure.title('Переход в раздел "История заказов"')
    @allure.description('Авторизуемся, затем нажимаем кнопку "Личный кабинет" в хэдере сайта. \n'
                        'На странице личного кабинета нажимаем ссылку на раздел "История заказов". \n'
                        'Проверяем, что ссылка стала активной и текущий url содержит путь "/account/order-history"')
    def test_transition_to_order_history(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_on_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_input_field(user["email"])
        login_page.fill_password_input_field(user["password"])
        login_page.click_login_button()
        header_page = HeaderPage(driver)
        header_page.click_on_profile_link_button()
        profile_page = ProfilePage(driver)
        profile_page.click_on_order_history_link()
        class_attribute_value_from_order_history_link = profile_page.check_order_history_link_is_active()
        current_url = profile_page.should_be_order_history_path_in_current_url()
        assert ('link_active' in class_attribute_value_from_order_history_link and
                '/account/order-history' in current_url)

    @allure.title('Переход в раздел "История заказов" и проверка последнего созданного заказа')
    @allure.description('Авторизуемся под пользователем у которого есть заказ, '
                        'затем нажимаем кнопку "Личный кабинет" в хэдере сайта. \n'
                        'На странице личного кабинета нажимаем ссылку на раздел "История заказов". \n'
                        'Проверяем, что отображаются корректные номер и название бургера '
                        'последнего заказа в истории заказов"')
    def test_transition_to_order_history_user_has_orders(self, driver, user, order):
        main_page = MainPage(driver)
        main_page.click_on_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_input_field(user["email"])
        login_page.fill_password_input_field(user["password"])
        login_page.click_login_button()
        header_page = HeaderPage(driver)
        header_page.click_on_profile_link_button()
        profile_page = ProfilePage(driver)
        profile_page.click_on_order_history_link()
        last_number_in_order_history = profile_page.check_last_order_number()
        burger_name_in_last_order = profile_page.check_burger_name_in_last_order()
        expected_order_number = str(order["order"]["number"])
        expected_burger_name = Burger.SPACE_METEORITE_FLUORESCENT_BURGER["name"]
        assert (expected_order_number in last_number_in_order_history and
                burger_name_in_last_order == expected_burger_name)

    @allure.title('Выход из аккаунта')
    @allure.description('Авторизуемся, затем нажимаем кнопку "Личный кабинет" в хэдере сайта. \n'
                        'На странице личного кабинета нажимаем кнопку "Выход". \n'
                        'Проверяем, что отобразилась страница логина с заголовком "Вход"')
    def test_account_logout(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_on_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_input_field(user["email"])
        login_page.fill_password_input_field(user["password"])
        login_page.click_login_button()
        header_page = HeaderPage(driver)
        header_page.click_on_profile_link_button()
        profile_page = ProfilePage(driver)
        profile_page.click_on_logout_button()
        heading_text_on_page = login_page.should_be_login_page_heading()
        assert heading_text_on_page == 'Вход'
