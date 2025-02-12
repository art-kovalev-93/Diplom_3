import allure
from locators.reset_password_page_locators import password_textbox, verify_code, show_password, password_field
from pages.base_page import BasePage



class ResetPasswordPage(BasePage):
    @allure.step('Ввести пароль')
    def enter_password(self):
        self.send_keys(password_textbox, "Qwerty123!")

    @allure.step('Ввести код подтверждения')
    def enter_verify_code(self):
        self.send_keys(verify_code, "123456")

    @allure.step('Нажать кнопку Показать пароль')
    def show_password(self):
        self.click_element(show_password)

    @allure.step('Проверяем, что пароль виден')
    def is_password_show(self):
        classes = self.get_object_classes(password_field)
        return "input__placeholder-focused" in classes
