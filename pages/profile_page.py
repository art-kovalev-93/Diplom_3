import allure
from locators.profile_page_locators import ORDER_HISTORY, LOGOUT, ORDER_COUNTER
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step('Нажать История заказов')
    def click_order_history(self):
        self.click_element(ORDER_HISTORY)

    @allure.step('Нажать Выход из заказа')
    def click_logout(self):
        self.click_element(LOGOUT)

    @allure.step('Получаем количество заказов')
    def get_order_number(self):
        return self.get_element_text(ORDER_COUNTER)