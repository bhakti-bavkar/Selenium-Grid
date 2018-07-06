from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_tmobile_login_page(local_driver):
    baseURL = "https://www.t-mobile.com/"
    wait = WebDriverWait(local_driver,10)
    local_driver.get(baseURL)
    assert 'T-Mobile' in local_driver.title
    #wait.until(EC.element_to_be_clickable((By.XPATH.'/html/body/header/nav/div[2]/button/span[2]'))).click()

