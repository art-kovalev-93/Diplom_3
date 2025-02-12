import allure
from locators.profile_page_locators import order_history_button, logout, order_counter
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step('Нажать История заказов')
    def click_order_history(self):
        self.click_element(order_history_button)

    @allure.step('Нажать Выход из заказа')
    def click_logout(self):
        self.click_element(logout)

    @allure.step('Получаем количество заказов')
    def get_order_number(self):
        return self.get_element_text(order_counter)