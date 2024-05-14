import allure

from pages.feed_page import FeedPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestOrderFeed:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Проверяем, что после клика на заказ в ленте заказов и открытия окна с деталями заказа '
                        'атрибут "class" тега "section" содержит строку "opened"')
    def test_click_on_order_opens_order_info_modal_window(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_on_order_feed_link_button()
        feed_page = FeedPage(driver)
        feed_page.click_on_first_order_in_order_feed_list()
        order_details_window_condition = feed_page.check_order_details_window_openness_condition()
        assert 'opened' in order_details_window_condition

    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    @allure.description('Авторизуемся под пользователем, у которого есть заказ. \n'
                        'В личном кабинете, в истории заказов получаем номер заказа.'
                        'Затем проверяем что заказ с таким номер отображается в ленте заказов')
    def test_user_orders_from_order_history_displayed_on_order_feed(self, driver, user, order):
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
        user_order_number = profile_page.check_last_order_number()
        header_page.click_on_order_feed_link_button()
        feed_page = FeedPage(driver)
        visibility_of_user_order = feed_page.check_visibility_of_user_order_in_order_feed(user_order_number)
        assert visibility_of_user_order is True

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description('Авторизуемся, проверяем значение счетчика "Выполнено за всё время" '
                        'на странице ленты заказов. Затем создаем заказ. \n'
                        'Проверяем, что значение счетчика стало больше')
    def test_completed_for_all_time_counter_increases(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_on_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_input_field(user["email"])
        login_page.fill_password_input_field(user["password"])
        login_page.click_login_button()
        header_page = HeaderPage(driver)
        header_page.click_on_order_feed_link_button()
        feed_page = FeedPage(driver)
        counter_completed_for_all_time_before = feed_page.check_completed_for_all_time_counter_value()
        header_page.click_on_constructor_link_button()
        main_page.transit_to_ingredient_section("Булки")
        main_page.drag_ingredient_on_order_basket("Флюоресцентная булка R2-D3")
        main_page.transit_to_ingredient_section("Соусы")
        main_page.drag_ingredient_on_order_basket("Соус фирменный Space Sauce")
        main_page.transit_to_ingredient_section("Начинки")
        main_page.drag_ingredient_on_order_basket("Мясо бессмертных моллюсков Protostomia")
        main_page.click_create_order()
        main_page.click_on_x_to_close_order_window()
        header_page.click_on_order_feed_link_button()
        feed_page = FeedPage(driver)
        counter_completed_for_all_time_after = feed_page.check_completed_for_all_time_counter_value()
        assert counter_completed_for_all_time_after > counter_completed_for_all_time_before

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description('Авторизуемся, проверяем значение счетчика "Выполнено за сегодня" '
                        'на странице ленты заказов. Затем создаем заказ. \n'
                        'Проверяем, что значение счетчика стало больше')
    def test_completed_today_counter_increases(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_on_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_input_field(user["email"])
        login_page.fill_password_input_field(user["password"])
        login_page.click_login_button()
        header_page = HeaderPage(driver)
        header_page.click_on_order_feed_link_button()
        feed_page = FeedPage(driver)
        counter_completed_today_before = feed_page.check_completed_today_counter_value()
        header_page.click_on_constructor_link_button()
        main_page.transit_to_ingredient_section("Булки")
        main_page.drag_ingredient_on_order_basket("Флюоресцентная булка R2-D3")
        main_page.transit_to_ingredient_section("Соусы")
        main_page.drag_ingredient_on_order_basket("Соус фирменный Space Sauce")
        main_page.transit_to_ingredient_section("Начинки")
        main_page.drag_ingredient_on_order_basket("Мясо бессмертных моллюсков Protostomia")
        main_page.click_create_order()
        main_page.click_on_x_to_close_order_window()
        header_page.click_on_order_feed_link_button()
        feed_page = FeedPage(driver)
        counter_completed_today_after = feed_page.check_completed_today_counter_value()
        assert counter_completed_today_after > counter_completed_today_before

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    @allure.description('С помощью API создаем заказ, переходим в ленту заказов,'
                        ' проверяем наличие номера созданного заказа в разделе "В работе"')
    def test_order_number_appears_in_work(self, driver, user, order):
        order_number = order["order"]["number"]
        header_page = HeaderPage(driver)
        header_page.click_on_order_feed_link_button()
        feed_page = FeedPage(driver)
        visibility_of_order_number_in_work = feed_page.check_visibility_of_order_number_in_work(str(order_number))
        assert visibility_of_order_number_in_work is True
