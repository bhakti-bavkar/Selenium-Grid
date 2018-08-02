from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class wait_for_display(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            return EC._find_element(driver, self.locator)
            # return element.value_of_css_property("display") == "block"
        except StaleElementReferenceException:
            return False






