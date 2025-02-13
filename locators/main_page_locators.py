from selenium.webdriver.common.by import By



LOGIN_BUTTON= [By.CSS_SELECTOR, ".mt-10 button"]
PROFILE = [By.CSS_SELECTOR, "[href='/account']"]
CONFIGURATOR = [By.CSS_SELECTOR, "[href='/'] .ml-2"]
FEED = [By.CSS_SELECTOR, "[href='/feed'] .ml-2"]
INGREDIENT = [By.CSS_SELECTOR, "img.ml-4"]
INGREDIENT_POPUP = [By.CSS_SELECTOR, "h2.text_type_main-large"]
CLOSE_INGREDIENT_POPUP = [By.CSS_SELECTOR, ".Modal_modal__close__TnseK svg"]
BURGER_CONSTRUCTOR_AREA = [By.CSS_SELECTOR, ".BurgerConstructor_basket__list__l9dp_"]
INGREDIENT_COUNTER = [By.CSS_SELECTOR, "p.counter_counter__num__3nue1"]
CREATE_ORDER_LOCATOR = [By.CSS_SELECTOR, ".BurgerConstructor_basket__container__2fUl3 button"]
ORDER_LOADER = [By.CSS_SELECTOR, "[alt='tick animation']"]
NEW_ORDER_COUNTER = [By.CSS_SELECTOR, "h2.Modal_modal__title__2L34m"]