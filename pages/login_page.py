import allure
from locators.login_page_locators import recovery_password, email_login, password, login_btn
from pages.base_page import BasePage
from test_data import USER_DATA


class LoginPage(BasePage):
    @allure.step('Нажать кнопку Восстановить пароль')
    def click_recovery_password(self):
        self.click_element(recovery_password)

    @allure.step('Выполнить логин под созданным пользователем.')
    def login(self):
        self.send_keys(email_login, USER_DATA.get('email'))
        self.send_keys(password, USER_DATA.get('password'))
        self.click_element(login_btn)