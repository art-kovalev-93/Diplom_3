import allure
from locators.reset_password_page_locators import PASSWORD_TEXTBOX, VERIFY_CODE, SHOW_PASSWORD, PASSWORD_FIELD
from pages.base_page import BasePage



class ResetPasswordPage(BasePage):
    @allure.step('Ввести пароль')
    def enter_password(self):
        self.send_keys(PASSWORD_TEXTBOX, "Qwerty123!")

    @allure.step('Ввести код подтверждения')
    def enter_verify_code(self):
        self.send_keys(VERIFY_CODE, "123456")

    @allure.step('Нажать кнопку Показать пароль')
    def show_password(self):
        self.click_element(SHOW_PASSWORD)

    @allure.step('Проверяем, что пароль виден')
    def is_password_show(self):
        classes = self.get_object_classes(PASSWORD_FIELD)
        return "input__placeholder-focused" in classes
