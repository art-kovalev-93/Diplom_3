from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = BASE_URL

    def find_element(self, locator, time = 5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find element {locator}')

    def click_element(self, locator):
        element = self.find_element(locator=locator)
        try:
            return element.click()
        except ElementClickInterceptedException:
            return self.driver.execute_script("arguments[0].click();", element)

    def click_i_obj(self, locator, i):
        return self.find_elements(locator = locator)[i].click()

    def get_element_text(self, locator):
        return self.find_element(locator=locator).text

    def find_elements(self, locator, time = 5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator), message=f'Not find elements {locator}')

    def wait_visibility_element(self, locator, time = 5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not find element {locator}')

    def current_url(self):
        return self.driver.current_url

    def send_keys(self, locator, text):
        return self.find_element(locator=locator).send_keys(text)

    def wait_url_to_be(self, url, time = 5):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(url))

    def open_next_tab(self):
        handles = self.driver.window_handles
        return self.driver.switch_to.window(handles[-1])

    def get_object_classes(self, locator):
        element = self.find_element(locator)
        classes = element.get_attribute('class').split(' ')
        return classes

    def get_text(self, locator):
        element_text = self.find_element(locator)
        return element_text.text

    def drag_and_drop(self, source_element, target_element):
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()

    def wait_text_in_element(self, locator, time = 30, text=""):
        try:
            return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutError:
            print("За 30 сек новый заказ не появился в списке.")
