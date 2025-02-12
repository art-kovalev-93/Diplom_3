import allure
from conftest import driver, new_user
from pages.forgot_password_page import RecoveryPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from urls import RECOVERY_PAGE_URL, RESET_PASSWORD_PAGE_URL


class TestRecoveryPasswordPage:
    @allure.title('Проверка открытия страницы восстановления пароля')
    def test_open_recovery_page_from_recovery_button_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_login()
        login_page = LoginPage(driver)
        login_page.click_recovery_password()
        recovery_page = RecoveryPage(driver)
        assert recovery_page.current_url() == RECOVERY_PAGE_URL

    @allure.title('Проверка отправки почты для восстановления пароля')
    def test_send_email_recovery_success(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.click_login()
        login_page = LoginPage(driver)
        login_page.click_recovery_password()
        recovery_page = RecoveryPage(driver)
        recovery_page.enter_email()
        recovery_page.click_recovery()
        reset_page = ResetPasswordPage(driver)
        reset_page.wait_url_to_be(RESET_PASSWORD_PAGE_URL)
        assert reset_page.current_url() == RESET_PASSWORD_PAGE_URL

    @allure.title('Проверка возможность показать введенный пароль')
    def test_show_password_reset_page_success(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.click_login()
        login_page = LoginPage(driver)
        login_page.click_recovery_password()
        recovery_page = RecoveryPage(driver)
        recovery_page.enter_email()
        recovery_page.click_recovery()
        reset_page = ResetPasswordPage(driver)
        reset_page.wait_url_to_be(RESET_PASSWORD_PAGE_URL)
        reset_page.enter_password()
        reset_page.show_password()
        assert reset_page.is_password_show()

