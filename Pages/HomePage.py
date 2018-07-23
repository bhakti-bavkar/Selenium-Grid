from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = {
            'logo': (By.CSS_SELECTOR, ".logo.t-mobile"),
            'link_logo': (By.CSS_SELECTOR, 'a[data-analytics-id*="-logo"]'),
            'link_menu': {
                'parent': (By.CSS_SELECTOR, 'div.nav-links'),
                'deals': (By.CSS_SELECTOR, 'a[data-analytics-id*="-link1"]'),
                'phones': (By.CSS_SELECTOR, 'a[data-analytics-id*="-link2"]'),
                'plans': (By.CSS_SELECTOR, 'a[data-analytics-id*="-link3"]'),
                'my_tmo': (By.CSS_SELECTOR, 'a[data-analytics-id*="-link4"]')
            },
            'side_menu': (By.CSS_SELECTOR, 'span.hamburger-text'),
            'freeze_screen': (By.CSS_SELECTOR, '.mute-screen.on')
        }
        self.menu = self.MenuBar(driver)

    def click_side_menu(self):
        menu = self.wait_for_element(25, EC.element_to_be_clickable, *self.elements['side_menu'])
        menu.click()

    def unfreeze_home_screen(self):
        self.get_element(*self.elements['freeze_screen']).click()

    class MenuBar(BasePage):
        def __init__(self, driver):
            super().__init__(driver)
            self.elements = {
                'menu_overlay': (By.ID, 'overlay-menu'),
                'unlimited_plan': (By.XPATH, '//a[contains(., "Unlimited plan")]'),
                'shop_phones': (By.XPATH, '//a[contains(., "Shop phones")]'),
                'watches_tablets': (By.XPATH, '//a[contains(., "Watches & tablets")]'),
                'Deals': (By.XPATH, '//a[contains(., "Deals")]'),
                'join_tmo': (By.XPATH, '//a[contains(., "Join T-Mobile")]'),
                'save': (By.XPATH, '//a[contains(., "See how much you could save")]'),
                'help': (By.XPATH, '//a[contains(., "We’ll help you join")]'),
                'bring_phone': (By.XPATH, '//a[contains(., "Bring your own phone")]'),
                'what_tmo': (By.XPATH, '//a[contains(., "What it\'s like on T-Mobile")]'),
                'coverage': (By.XPATH, '//a[contains(., "Check out the coverage")]'),
                'inter_calls': (By.XPATH, '//a[contains(., "International calling")]'),
                'travel_abroad': (By.XPATH, '//a[contains(., "Traveling abroad")]'),
                'wireless': (By.XPATH, '//a[contains(., "More than wireless")]'),
                'smart_devices': (By.XPATH, '//a[contains(., "Smart devices")]'),
                'multiple_numbers': (By.XPATH, '//a[contains(., "Use multiple numbers on my phone")]'),
                'accessories': (By.XPATH, '//a[contains(., "Accessories")]')
            }



