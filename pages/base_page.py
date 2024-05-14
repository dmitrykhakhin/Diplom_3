from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        locator = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(locator).click(on_element=locator).perform()

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_value_from_element_attribute(self, locator, name_of_attribute):
        return self.find_element_with_wait(locator).get_attribute(name_of_attribute)

    def get_current_url(self):
        return self.driver.current_url

    def drag_and_drop_element(self, locator_from, locator_to):
        locator_from = self.find_element_with_wait(locator_from)
        locator_to = self.find_element_with_wait(locator_to)
        ActionChains(self.driver).drag_and_drop(locator_from, locator_to).perform()

    def check_element_is_visible(self, locator):
        self.find_element_with_wait(locator)
        if expected_conditions.visibility_of_element_located(locator) is not None:
            return True
        else:
            return False

    @staticmethod
    def format_locator(unformatted_locator, value):
        method, locator = unformatted_locator
        locator = locator.format(value)
        formatted_locator = method, locator
        return formatted_locator
