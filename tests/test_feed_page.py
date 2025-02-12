import allure

from api.order_api import OrderApi
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from receip_generator import Generator
from conftest import driver, new_user



class TestFeedPage:
    @allure.title('Проверка открытия окна с подробной информацией о заказе')
    def test_open_order_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed()
        feed = FeedPage(driver)
        feed.click_on_order()
        assert feed.is_order_popup_displayed()

    @allure.title('Проверка наличия заказа пользователя в Ленте заказов')
    def test_user_order_in_feed(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.click_login()
        login_p = LoginPage(driver)
        login_p.login()
        main_page.click_profile()
        profile = ProfilePage(driver)
        profile.click_order_history()
        number = profile.get_order_number()
        main_page.click_feed()
        feed = FeedPage(driver)
        assert feed.is_order_on_feed(number)

    @allure.title('Проверка что счетчик заказов увеличивается')
    def test_order_counter_success(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.click_feed()
        feed = FeedPage(driver)
        order_number = feed.get_all_orders_number()
        order = OrderApi()
        order.create_order(access_token=new_user.json().get('accessToken'), ingredients=Generator.get_receipt())
        feed.wait_new_order(order_number)
        new_order_number = feed.get_all_orders_number()
        assert int(order_number) < int(new_order_number)

    @allure.title('Проверка что новый заказ появляется В работе')
    def test_order_number_in_work_success(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.click_feed()
        feed = FeedPage(driver)
        order_number = feed.get_all_orders_number()
        order = OrderApi()
        order.create_order(access_token=new_user.json().get('accessToken'), ingredients=Generator.get_receipt())
        feed.wait_new_order_in_work(order_number)
        assert feed.wait_new_order_in_work(order_number) == int(order_number)+1
