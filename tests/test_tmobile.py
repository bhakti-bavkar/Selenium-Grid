from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helper import element_helper as help


class TestTMOHome:
    def test_tmo_home_page(self, driver):
        driver.get('http://www.t-mobile.com')
        WebDriverWait(driver,25).until(EC.title_contains('T-Mobile'))
        assert 'Cell Phones | 4G Phones | iPhone and Android Phones | T-Mobile' in driver.title

        logo = driver.find_element(By.CSS_SELECTOR, ".logo.t-mobile")
        home_link = logo.find_element(By.CSS_SELECTOR, 'a[data-analytics-id*="-logo"]')
        assert 'www.t-mobile.com' in home_link.get_attribute('href')

        nav_links = driver.find_element(By.CSS_SELECTOR, 'div.nav-links')

        deals = nav_links.find_element(By.CSS_SELECTOR, 'a[data-analytics-id*="-link1"]')
        assert deals.text == 'DEALS'
        assert 'www.t-mobile.com/offers/deals-hub' in deals.get_attribute('href')

        phones = nav_links.find_element(By.CSS_SELECTOR, 'a[data-analytics-id*="-link2"]')
        assert phones.text == 'PHONES'
        assert 'www.t-mobile.com/cell-phones' in phones.get_attribute('href')

        plans = nav_links.find_element(By.CSS_SELECTOR, 'a[data-analytics-id*="-link3"]')
        assert plans.text == 'PLANS'
        assert 'www.t-mobile.com/cell-phone-plans' in plans.get_attribute('href')

        my_tmo = nav_links.find_element(By.CSS_SELECTOR, 'a[data-analytics-id*="-link4"]')
        assert my_tmo.text == 'MY T-MOBILE'
        assert 'my.t-mobile.com' in my_tmo.get_attribute('href')

    def test_tmo_menu_selected(self, driver):
        driver.get('http://www.t-mobile.com')
        wait = WebDriverWait(driver,25)
        wait.until(EC.title_contains('T-Mobile'))
        menu_text = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.hamburger-text')))
        assert 'MENU' in menu_text.text
        menu_text.click()

        menu_overlay = driver.find_element(By.ID, 'overlay-menu')
        assert 'visibility: visible' in menu_overlay.get_attribute('style')

        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "Unlimited plan")]'), 'Unlimited plan')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "Shop phones")]'), 'Shop phones')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "Watches & tablets")]'), 'Watches & tablets')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "Deals")]'), 'Deals')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//div[contains(., "Join T-Mobile")]'), 'Join T-Mobile')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "See how much you could save")]'), 'See how much you could save')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "We’ll help you join")]'), 'We’ll help you join')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "Bring your own phone")]'), 'Bring your own phone')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//div[contains(., "What it\'s like on T-Mobile")]'), 'What it\'s like on T-Mobile')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "Check out the coverage")]'), 'Check out the coverage')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "International calling")]'), 'International calling')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "Traveling abroad")]'), 'Traveling abroad')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//div[contains(., "More than wireless")]'), 'More than wireless')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "Smart devices")]'), 'Smart devices')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "Use multiple numbers on my phone")]'), 'Use multiple numbers on my phone')
        help.check_element_visible(menu_overlay,
                                         (By.XPATH, '//a[contains(., "Accessories")]'), 'Accessories')

        # Check that Home Page freezes and nothing gets clicked except in Menu Bar
        help.check_element_visible(driver, (By.CSS_SELECTOR, '.mute-screen.on'), 'Home Page is not accessible')

    def test_tmo_menu_unselected(self, driver):
        driver.get('http://www.t-mobile.com')
        WebDriverWait(driver,25).until(EC.title_contains('T-Mobile'))
        # select Menu
        driver.find_element(By.CSS_SELECTOR, 'span.hamburger-text').click()
        # unselect Menu
        driver.find_element(By.CSS_SELECTOR,'.mute-screen').click()
        menu_overlay = driver.find_element(By.ID, 'overlay-menu')
        assert 'visibility: hidden' in menu_overlay.get_attribute('style')


