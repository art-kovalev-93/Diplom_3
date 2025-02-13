import allure

from locators.main_page_locators import LOGIN_BUTTON, PROFILE, CONFIGURATOR, FEED, INGREDIENT, INGREDIENT_POPUP, \
    CLOSE_INGREDIENT_POPUP, BURGER_CONSTRUCTOR_AREA, CREATE_ORDER_LOCATOR, ORDER_LOADER, NEW_ORDER_COUNTER
from pages.base_page import BasePage
from pages.login_page import LoginPage



class MainPage(BasePage):
    @allure.step('Нажать кнопку Войти в аккаунт')
    def click_login(self):
        self.click_element(LOGIN_BUTTON)

    @allure.step('Нажать кнопку Личный кабинет')
    def click_profile(self):
        self.click_element(PROFILE)

    @allure.step('Нажать конструктор в хидере')
    def click_configurator(self):
        self.click_element(CONFIGURATOR)

    @allure.step('Нажать Лента заказов в хидере')
    def click_feed(self):
        self.click_element(FEED)

    def login_if_need(self, user):
        if user == "auth":
            MainPage.click_login(self)
            LoginPage.login(self)

    @allure.step('Нажать на ингредиент в конструкторе')
    def click_ingredient(self):
        self.click_element(INGREDIENT)

    @allure.step('Записываем текст из попап окна игредиента.')
    def get_ingredient_popup_text(self):
        return self.get_element_text(INGREDIENT_POPUP)

    @allure.step('Закрыть окно с информацией об ингредиенте')
    def close_ingredient_popup(self):
        self.click_element(CLOSE_INGREDIENT_POPUP)

    @allure.step('Проверяем, что окно с информацией об ингредиенте закрыто')
    def close_and_check_ingredient_popup(self):
        popup = self.find_element(INGREDIENT_POPUP)
        MainPage.close_ingredient_popup(self)
        return popup.is_displayed()

    @allure.step('Перетягиваем ингредиент в зону сборки гамбургера')
    def drag_and_drop_ingredient(self):
        source_element = self.find_element(INGREDIENT)
        target_element = self.find_element(BURGER_CONSTRUCTOR_AREA)
        self.drag_and_drop(source_element=source_element, target_element=target_element)

    @allure.step('Нажать Оформить заказ')
    def click_create_order(self):
        self.click_element(CREATE_ORDER_LOCATOR)

    @allure.step('Ожидаем появление информации о создании заказа')
    def wait_order_loader(self):
        self.wait_visibility_element(ORDER_LOADER)

    @allure.step('Проверяем, что заказ создан.')
    def is_new_order_created(self):
        return self.find_element(NEW_ORDER_COUNTER).is_displayed()

