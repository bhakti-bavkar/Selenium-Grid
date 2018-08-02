import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Config import DRIVER_PATH


# caps['browserName'] = 'Chrome'
# caps['deviceName'] = 'Nexus 6P'
# caps['platformVersion'] = '7.0'
# caps['platformName'] = 'Android'
# caps['deviceOrientation'] = 'portrait'


class DriverConfig:
    # Browser, Browser Version, Platform
    cross_browser_config = [('chrome', '', 'ANY'),
                            ('firefox', '', 'ANY')]
                            #('chrome', '', 'Android')]
    hub = 'http://10.206.8.26:4444/wd/hub'

    @classmethod
    def get_driver_list(cls):
        drivers = []
        for node in cls.cross_browser_config:
            driver_name = node[0] + '-' + node[1] + '-' + node[2]
            drivers.append(driver_name)
        return drivers

    @classmethod
    def get_local_driver(cls, driver, executable_path):
        return driver(executable_path=executable_path)

    @classmethod
    def get_remote_webdriver(cls, desired_capabilities):
        print("\n starting %s" % desired_capabilities["browserName"])
        return webdriver.Remote(command_executor=cls.hub, desired_capabilities=desired_capabilities)

    @classmethod
    def get_local_driver_config(cls, config):
        config = config.split('-')
        browser = config[0]
        if browser.lower() == 'firefox':
            driver = webdriver.Firefox
            executable_path = os.path.join(DRIVER_PATH, 'geckodriver.exe')
        elif browser.lower() == 'chrome':
            driver = webdriver.Chrome
            executable_path = os.path.join(DRIVER_PATH, 'chromedriver.exe')
        elif browser.lower() == 'ie':
            driver = webdriver.Ie
            executable_path = os.path.join(DRIVER_PATH, 'IEDriverServer.exe')
        else:
            driver = None
            executable_path = ''
        return cls.get_local_driver(driver, executable_path)

    @classmethod
    def get_remote_driver_config(cls, config):
        config = config.split('-')
        browser = config[0]
        if browser.lower() == 'firefox':
            desired_capabilities = DesiredCapabilities.FIREFOX.copy()
        elif browser.lower() == 'chrome':
            if config[2].lower() in ['any', 'vista', 'windows', 'win10']:
                desired_capabilities = DesiredCapabilities.CHROME.copy()
            else: # Android
                desired_capabilities = DesiredCapabilities.ANDROID.copy()
                desired_capabilities['browserName'] = 'chrome'
                desired_capabilities["platformName"] = 'Android'
                desired_capabilities["platformVersion"] = '7.1.1'
        elif browser.lower() == 'ie':
            desired_capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
        else:
            desired_capabilities = {}
        desired_capabilities['version'] = config[1]
        desired_capabilities['platform'] = config[2]
        return cls.get_remote_webdriver(desired_capabilities)

