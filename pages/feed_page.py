from locators.feed_locators import order, order_popup, order_number, order_number_in_work
from locators.feed_locators import all_orders_counter
from pages.base_page import BasePage
import allure


class FeedPage(BasePage):
    @allure.step('Нажать на последний заказ в Ленте заказов')
    def click_on_order(self):
        self.click_element(order)

    @allure.step('Проверяем, что открылось окно с информацией о заказе.')
    def is_order_popup_displayed(self):
        return self.find_element(order_popup).is_displayed()

    @allure.step('Проверяем, что заказ пользователя есть в ленте заказов')
    def is_order_on_feed(self, number):
        numbers = self.find_elements(order_number)
        for i in numbers:
            if number == i.text:
                return True
        return False

    @allure.step('Записываем количество заказов, выполненных за все время.')
    def get_all_orders_number(self):
        return self.get_element_text(all_orders_counter)

    @allure.step('Ожидаем новый заказ')
    def wait_new_order(self, number):
        self.wait_text_in_element(locator=all_orders_counter, text=str(int(number)+1))

    @allure.step('Ожидаем новый заказ в работе')
    def wait_new_order_in_work(self, number):
        return self.wait_text_in_element(locator=order_number_in_work, text=str(int(number) + 1))