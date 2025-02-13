from locators.feed_locators import ORDER, ORDER_POPUP, ORDER_NUMBER, ORDER_NUMBER_IN_WORK
from locators.feed_locators import ALL_ORDER_COUNTER
from pages.base_page import BasePage
import allure


class FeedPage(BasePage):
    @allure.step('Нажать на последний заказ в Ленте заказов')
    def click_on_order(self):
        self.click_element(ORDER)

    @allure.step('Проверяем, что открылось окно с информацией о заказе.')
    def is_order_popup_displayed(self):
        return self.find_element(ORDER_POPUP).is_displayed()

    @allure.step('Проверяем, что заказ пользователя есть в ленте заказов')
    def is_order_on_feed(self, number):
        numbers = self.find_elements(ORDER_NUMBER)
        for i in numbers:
            if number == i.text:
                return True
        return False

    @allure.step('Записываем количество заказов, выполненных за все время.')
    def get_all_orders_number(self):
        return self.get_element_text(ALL_ORDER_COUNTER)

    @allure.step('Ожидаем новый заказ')
    def wait_new_order(self, number):
        self.wait_text_in_element(locator=ALL_ORDER_COUNTER, text=str(int(number) + 1))

    @allure.step('Ожидаем новый заказ в работе')
    def wait_new_order_in_work(self, number):
        self.wait_text_in_element(locator=ORDER_NUMBER_IN_WORK, text=str(int(number) + 1))

    @allure.step('Получаем номер заказа в работе')
    def get_order_in_work(self):
         return self.find_element(ORDER_NUMBER_IN_WORK).text