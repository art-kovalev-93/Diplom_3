import allure
from locators.forgot_password_locators import email_textbox, recovery_button
from pages.base_page import BasePage
from test_data import USER_DATA


class RecoveryPage(BasePage):
    @allure.step('Ввести почту в поле Почта')
    def enter_email(self):
        self.send_keys(email_textbox, USER_DATA.get('email'))

    @allure.step('Нажать кнопку Восстановить пароль')
    def click_recovery(self):
        self.click_element(recovery_button)
