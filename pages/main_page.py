import allure

from locators.main_page_locators import login_button, profile, congigurator, feed, ingredient, ingredient_detail_popup, \
    close_ingredient_popup, burger_constructor_area, create_order_locator, order_loader, new_order_counter_popup
from pages.base_page import BasePage
from pages.login_page import LoginPage



class MainPage(BasePage):
    @allure.step('Нажать кнопку Войти в аккаунт')
    def click_login(self):
        self.click_element(login_button)

    @allure.step('Нажать кнопку Личный кабинет')
    def click_profile(self):
        self.click_element(profile)

    @allure.step('Нажать конструктор в хидере')
    def click_configurator(self):
        self.click_element(congigurator)

    @allure.step('Нажать Лента заказов в хидере')
    def click_feed(self):
        self.click_element(feed)

    def login_if_need(self, user):
        if user == "auth":
            MainPage.click_login(self)
            LoginPage.login(self)

    @allure.step('Нажать на ингредиент в конструкторе')
    def click_ingredient(self):
        self.click_element(ingredient)

    @allure.step('Записываем текст из попап окна игредиента.')
    def get_ingredient_popup_text(self):
        return self.get_element_text(ingredient_detail_popup)

    @allure.step('Закрыть окно с информацией об ингредиенте')
    def close_ingredient_popup(self):
        self.click_element(close_ingredient_popup)

    @allure.step('Проверяем, что окно с информацией об ингредиенте закрыто')
    def close_and_check_ingredient_popup(self):
        popup = self.find_element(ingredient_detail_popup)
        MainPage.close_ingredient_popup(self)
        return popup.is_displayed()

    @allure.step('Перетягиваем ингредиент в зону сборки гамбургера')
    def drag_and_drop_ingredient(self):
        source_element = self.find_element(ingredient)
        target_element = self.find_element(burger_constructor_area)
        self.drag_and_drop(source_element=source_element, target_element=target_element)

    @allure.step('Нажать Оформить заказ')
    def click_create_order(self):
        self.click_element(create_order_locator)

    @allure.step('Ожидаем появление информации о создании заказа')
    def wait_order_loader(self):
        self.wait_visibility_element(order_loader)

    @allure.step('Проверяем, что заказ создан.')
    def is_new_order_created(self):
        return self.find_element(new_order_counter_popup).is_displayed()

