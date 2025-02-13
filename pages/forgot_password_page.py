import allure
from locators.forgot_password_locators import EMAIL_TEXTBOX, RECOVERY_BUTTON
from pages.base_page import BasePage
from test_data import USER_DATA


class RecoveryPage(BasePage):
    @allure.step('Ввести почту в поле Почта')
    def enter_email(self):
        self.send_keys(EMAIL_TEXTBOX, USER_DATA.get('email'))

    @allure.step('Нажать кнопку Восстановить пароль')
    def click_recovery(self):
        self.click_element(RECOVERY_BUTTON)
