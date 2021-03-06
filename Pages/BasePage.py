from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from helper import element_helper as Help


class BasePage:
    def __init__(self, driver, base_url='http://www.t-mobile.com'):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.base_url = base_url
        self.elements = {}

    def open(self):
        self.driver.get(self.base_url)

    def get_page_title(self):
        return self.driver.title

    def get_element(self, *locator):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return "Element can not be found on page"

    def wait_for_element(self, timeout=5, condition=None, *locator):
        wait = WebDriverWait(self.driver, timeout, poll_frequency=0.1)
        try:
            return wait.until(condition(locator))
        except TimeoutException:
            return False
        except StaleElementReferenceException:
            return False

    def wait_for_page(self, condition, title, timeout=5):
        wait = WebDriverWait(self.driver, timeout, poll_frequency=0.1)
        try:
            return wait.until(condition(title))
        except TimeoutException:
            return False

    def wait_for_change(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout, poll_frequency=0.1)
        return wait.until(Help.wait_for_display(locator))

    def page_elements_present(self, elements):
        if len(elements) <= 0:
            return True
        parent = elements.get('parent')
        if parent is None:
            parent = self.driver
        else:
            parent = self.get_element(parent)
        for element, locator in elements.items():
            if element == 'parent':
                continue
            if type(element) is dict:
                status = self.page_elements_present(element)
                if not status:
                    return False
                continue
            status = self.check_element_visible(parent, *locator)
            if not status:
                print("Element not found: " + str(element))
                return False
            return True

    def check_element_visible(self, parent=None, *locator):
        try:
            if parent is None:
                parent = self.driver
            return parent.find_element(*locator)
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False

