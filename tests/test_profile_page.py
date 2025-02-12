import allure
from conftest import driver, new_user
from locators.profile_page_locators import orders
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import LOGIN_PAGE_URL, PROFILE_PAGE_URL, ORDER_HISTORY_URL


class TestProfilePage:
    @allure.title('Проверка открытия ЛК не авторизированным пользователем')
    def test_open_profile_unauth_user(self, driver):
        main_page = MainPage(driver)
        main_page.click_profile()
        assert main_page.current_url() == LOGIN_PAGE_URL

    @allure.title('Проверка открытия ЛК авторизированным пользователем')
    def test_open_profile_auth_user(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.click_login()
        login_page = LoginPage(driver)
        login_page.login()
        main_page.click_profile()
        main_page.wait_url_to_be(PROFILE_PAGE_URL)
        assert main_page.current_url() == PROFILE_PAGE_URL

    @allure.title('Проверка истории заказов пользователя')
    def test_order_history_user_success(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.click_login()
        login_page = LoginPage(driver)
        login_page.login()
        main_page.click_profile()
        main_page.wait_url_to_be(PROFILE_PAGE_URL)
        profile = ProfilePage(driver)
        profile.click_order_history()
        profile.wait_url_to_be(ORDER_HISTORY_URL)
        assert len(profile.find_elements(orders)) == 1 and profile.current_url() == ORDER_HISTORY_URL

    @allure.title('Проверка разлогина')
    def test_logout_success(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.click_login()
        login_page = LoginPage(driver)
        login_page.login()
        main_page.click_profile()
        main_page.wait_url_to_be(PROFILE_PAGE_URL)
        profile = ProfilePage(driver)
        profile.click_logout()
        profile.wait_url_to_be(LOGIN_PAGE_URL)
        assert profile.current_url() == LOGIN_PAGE_URL