import allure
import pytest

from pages.feed_page import FeedPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestBasicFunctionality:
    @allure.title('Переход по клику кнопки "Конструктор" в хедере на главную страницу')
    @allure.description('Входим на страницу логина, затем по клику на кнопку "Конструктор" в хедере '
                        'переходим на главную страницу и проверяем наличие заголовка "Соберите бургер"')
    def test_transition_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.should_be_login_page_heading()
        header_page = HeaderPage(driver)
        header_page.click_on_constructor_link_button()
        constructor_heading_text = main_page.should_be_constructor_heading()
        assert constructor_heading_text == 'Соберите бургер'

    @allure.title('Переход по клику кнопки "Лента заказов" в хедере на страницу ленты заказов')
    @allure.description('Проверяем, что находимся на главной страницы, \n'
                        'затем по клику на кнопку "Лента заказов" в хедере переходим на на страницу ленты заказов '
                        'и проверяем наличие заголовка "Лента заказов"')
    def test_transition_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.should_be_constructor_heading()
        header_page = HeaderPage(driver)
        header_page.click_on_order_feed_link_button()
        feed_page = FeedPage(driver)
        assert feed_page.should_be_order_feed_heading() == 'Лента заказов'

    @allure.title('Клик на ингредиент, открывает всплывающее окно с деталями')
    @allure.description('Проверяем, что после клика на ингредиент и открытия окна "Детали ингредиента" '
                        'атрибут "class" тега "section" содержит строку "open"')
    def test_clicks_on_ingredient_opens_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        status_of_window_openness = main_page.check_ingredient_window_openness_condition()
        assert 'open' in status_of_window_openness

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    @allure.description('Проверяем, что после клика на крестик в окне "Детали ингредиента" '
                        'атрибут "class" тега "section" НЕ содержит строку "open"')
    def test_click_on_x_to_close_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.click_on_x_to_close_ingredient_window()
        status_of_window_openness = main_page.check_ingredient_window_openness_condition()
        assert 'open' not in status_of_window_openness

    @pytest.mark.parametrize(
        "section, ingredient, expected_counter", [
            ("Булки", "Краторная булка N-200i", 2),
            ("Соусы", "Соус Spicy-X", 1),
            ("Начинки", "Говяжий метеорит (отбивная)", 1)
        ]
    )
    @allure.title('При добавлении ингредиента в заказ, счётчик этого ингредиента увеличивается')
    @allure.description(f'Перетаскиваем заданный ингредиент в корзину заказа и проверяем,'
                        f' что счетчик ингредиента увеличился')
    def test_after_adding_to_order_ingredient_counter_increases(self, driver, section, ingredient, expected_counter):
        main_page = MainPage(driver)
        main_page.transit_to_ingredient_section(section)
        counter_before = main_page.check_ingredient_counter(ingredient)
        main_page.drag_ingredient_on_order_basket(ingredient)
        counter_after = main_page.check_ingredient_counter(ingredient)
        assert int(counter_after) > int(counter_before) and int(counter_after) == int(expected_counter)

    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('Авторизуемся, добавляем ингредиенты в корзину и нажимаем кнопку "Оформить заказ" \n'
                        'Проверяем, что в модальном окне с информацией о созданном заказе '
                        'есть строка "Ваш заказ начали готовить"')
    def test_authorized_user_can_create_order(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_on_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_input_field(user["email"])
        login_page.fill_password_input_field(user["password"])
        login_page.click_login_button()
        main_page.transit_to_ingredient_section("Булки")
        main_page.drag_ingredient_on_order_basket("Флюоресцентная булка R2-D3")
        main_page.transit_to_ingredient_section("Соусы")
        main_page.drag_ingredient_on_order_basket("Соус фирменный Space Sauce")
        main_page.transit_to_ingredient_section("Начинки")
        main_page.drag_ingredient_on_order_basket("Мясо бессмертных моллюсков Protostomia")
        main_page.click_create_order()
        text_from_opened_modal_window = main_page.should_be_text_in_created_order_info_window()
        assert text_from_opened_modal_window == "Ваш заказ начали готовить"
