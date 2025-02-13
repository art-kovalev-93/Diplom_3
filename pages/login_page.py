import allure
from locators.login_page_locators import RECOVERY_PASSWORD, EMAIL_LOGIN, PASSWORD, LOGIN_BTN
from pages.base_page import BasePage
from test_data import USER_DATA


class LoginPage(BasePage):
    @allure.step('Нажать кнопку Восстановить пароль')
    def click_recovery_password(self):
        self.click_element(RECOVERY_PASSWORD)

    @allure.step('Выполнить логин под созданным пользователем.')
    def login(self):
        self.send_keys(EMAIL_LOGIN, USER_DATA.get('email'))
        self.send_keys(PASSWORD, USER_DATA.get('password'))
        self.click_element(LOGIN_BTN)