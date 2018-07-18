from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def get_tmo_home(driver):
    baseURL = "https://www.t-mobile.com/"
    driver.get(baseURL)
    yield
    driver.close()


def test_tmo_login_page(get_tmo_home, driver):
    assert 'T-Mobile' in driver.title

    logo = driver.find_element((By.CSS_SELECTOR,".logo.t-mobile"))
    home_link = logo.find_element((By.XPATH,'//*[@data-analytics-id="-logo"]'))
    assert home_link.get_attribute('href') == "http://www.t-mobile.com"

    deals = driver.find_element((By.CSS_SELECTOR,'a[aria-label="Deals"]'))
    assert deals.text == 'Deals'
    assert 'www.t-mobile.com/offers/deals-hub' in deals.get_attribute('href')

    phones = driver.find_element((By.CSS_SELECTOR,'a[aria-label="Plans"]'))
    assert phones.text == 'Plans'
    assert 'www.t-mobile.com/cell-phones' in phones.get_attribute('href')

    plans = driver.find_element((By.CSS_SELECTOR,'a[aria-label="Plans"]'))
    assert plans.text == 'Plans'
    assert 'www.t-mobile.com/cell-phone-plans' in plans.get_attribute('href')

    my_tmo = driver.find_element((By.CSS_SELECTOR,'a[aria-label="My T-Mobile"]'))
    assert my_tmo.text == 'My T-Mobile'
    assert 'my.t-mobile.com' in my_tmo.get_attribute('href')


def test_tmo_menu(get_tmo_home, driver):
    #wait.until(EC.element_to_be_clickable((By.XPATH.'/html/body/header/nav/div[2]/button/span[2]'))).click()
    assert 'T-Mobile' in driver.title

