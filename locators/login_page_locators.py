from selenium.webdriver.common.by import By


RECOVERY_PASSWORD = [By.CSS_SELECTOR, "[href='/forgot-password']"]
EMAIL_LOGIN = [By.CSS_SELECTOR, ".input__textfield[name='name']"]
PASSWORD = [By.CSS_SELECTOR, "[type='password']"]
LOGIN_BTN = [By.CSS_SELECTOR, "form button"]