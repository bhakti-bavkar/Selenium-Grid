from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from CommonLib import elementLib, supportLib


class TestTMOHome:
    # def test_tmo_home_page(self, driver):
    #     driver.get('http://www.t-mobile.com')
    #     WebDriverWait(driver,25).until(EC.title_contains('T-Mobile'))
    #     assert 'Cell Phones | 4G Phones | iPhone and Android Phones | T-Mobile' in driver.title
    #
    #     logo = driver.find_element(By.CSS_SELECTOR, ".logo.t-mobile")
    #     home_link = logo.find_element(By.CSS_SELECTOR, 'a[data-analytics-id*="-logo"]')
    #     assert 'www.t-mobile.com' in home_link.get_attribute('href')
    #
    #     nav_links = driver.find_element(By.CSS_SELECTOR, 'div.nav-links')
    #
    #     deals = nav_links.find_element(By.CSS_SELECTOR, 'a[data-analytics-id*="-link1"]')
    #     assert deals.text == 'DEALS'
    #     assert 'www.t-mobile.com/offers/deals-hub' in deals.get_attribute('href')
    #
    #     phones = nav_links.find_element(By.CSS_SELECTOR, 'a[data-analytics-id*="-link2"]')
    #     assert phones.text == 'PHONES'
    #     assert 'www.t-mobile.com/cell-phones' in phones.get_attribute('href')
    #
    #     plans = nav_links.find_element(By.CSS_SELECTOR, 'a[data-analytics-id*="-link3"]')
    #     assert plans.text == 'PLANS'
    #     assert 'www.t-mobile.com/cell-phone-plans' in plans.get_attribute('href')
    #
    #     my_tmo = nav_links.find_element(By.CSS_SELECTOR, 'a[data-analytics-id*="-link4"]')
    #     assert my_tmo.text == 'MY T-MOBILE'
    #     assert 'my.t-mobile.com' in my_tmo.get_attribute('href')

    def test_tmo_menu_selected(self, driver):
        driver.get('http://www.t-mobile.com')
        wait = WebDriverWait(driver,25)
        wait.until(EC.title_contains('T-Mobile'))
        menu_text = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.hamburger-text')))
        assert 'MENU' in menu_text.text
        menu_text.click()

        menu_overlay = driver.find_element(By.ID, 'overlay-menu')
        assert 'visibility: visible' in menu_overlay.get_attribute('style')
        supportLib.check_element_visible(menu_overlay, (By.CSS_SELECTOR, 'button.close'), 'Button Close')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "My T-Mobile")]'), 'My T-Mobile')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Plans")]'), 'Plans')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "My T-Mobile")]'), 'T-Mobile ONE')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Prepaid Plans")]'), 'Prepaid Plans')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Phones")]'), 'Phones')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Tablets & Devices")]'), 'Tablet&Devices')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Connected Devices")]'), 'Connected Devices')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Wearable Tech")]'), 'Wearable Tech')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Accessories")]'), 'Accessories')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Bring Your Own Phone")]'), 'Bring Your Own Phone')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Prepaid Phones")]'), 'Prepaid Phones')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Bring Your Own Tablet")]'), 'Bring Your Own Tablet')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Deals")]'), 'Deals')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "T-Mobile Magenta Gear")]'), 'T-Mobile Magenta Gear')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Coverage")]'), 'Coverage')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Compare Carriers")]'), 'Compare Carriers')
        supportLib.check_element_visible(menu_overlay, (By.XPATH, '//a[contains(., "Coverage Map")]'), 'Coverage Map')

        # Check that Home Page freezes and nothing gets clicked except in Menu Bar
        supportLib.check_element_visible(driver, (By.CSS_SELECTOR, '.mute-screen.on'), 'Home Page is accessible')

    def test_tmo_menu_unselected(self, driver):
        driver.get('http://www.t-mobile.com')
        WebDriverWait(driver,25).until(EC.title_contains('T-Mobile'))
        driver.find_element(By.CSS_SELECTOR, 'span.hamburger-text').click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.close'))).click()
        menu_overlay = driver.find_element(By.ID, 'overlay-menu')
        assert 'visibility: hidden' in menu_overlay.get_attribute('style')


