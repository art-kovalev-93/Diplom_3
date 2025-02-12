from selenium.webdriver.common.by import By


recovery_password = [By.CSS_SELECTOR, "[href='/forgot-password']"]
email_login = [By.CSS_SELECTOR, ".input__textfield[name='name']"]
password = [By.CSS_SELECTOR, "[type='password']"]
login_btn = [By.CSS_SELECTOR, "form button"]