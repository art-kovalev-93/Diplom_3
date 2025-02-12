import allure
from locators.main_page_locators import ingredient_counter
from pages.login_page import LoginPage
from pages.main_page import MainPage
from test_data import DETAIL_INGREDIENT_POPUP_TEXT
from urls import BASE_URL, FEED_URL, INGREDIENT_URL
from conftest import driver, new_user
import pytest


class TestMainPage:
    @allure.title('Проверка открытия Конструктора')
    @pytest.mark.parametrize('user', ["auth","unauth"])
    def test_open_configurator_success(self, driver, user, new_user):
        main_page= MainPage(driver)
        main_page.login_if_need(user)
        main_page.click_feed()
        main_page.click_configurator()
        assert main_page.current_url() == BASE_URL

    @allure.title('Проверка открытия Ленты заказов')
    @pytest.mark.parametrize('user', ["auth", "unauth"])
    def test_open_feed_success(self, driver, user, new_user):
        main_page = MainPage(driver)
        main_page.login_if_need(user)
        main_page.click_feed()
        assert main_page.current_url() == FEED_URL

    @allure.title('Проверка открытия подробной информации об ингредиенте')
    def test_open_ingredient_details_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.get_ingredient_popup_text() == DETAIL_INGREDIENT_POPUP_TEXT and INGREDIENT_URL in main_page.current_url()

    @allure.title('Проверка закрытия окна с информацией об ингредиенте')
    def test_close_ingredient_details_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.close_and_check_ingredient_popup()

    @allure.title('Проверка увеличения количества ингредиентов, добавленных в заказ')
    def test_ingredient_counter_success(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()
        assert main_page.get_element_text(ingredient_counter) == "2"

    @allure.title('Проверка создания заказа авторизированным пользователем')
    def test_create_order_auth_success(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.click_login()
        login_p = LoginPage(driver)
        login_p.login()
        main_page.drag_and_drop_ingredient()
        main_page.click_create_order()
        main_page.wait_order_loader()
        assert main_page.is_new_order_created()






