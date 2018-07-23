import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Config import DRIVER_PATH
from selenium.webdriver.firefox.options import Options

browsers = ["chrome", "firefox"]#, "IE"]
chrome_versions = []#, "50"]
firefox_versions = []
ie_versions = []
platforms = ["VISTA"]#, "8.1"]

# caps['browserName'] = 'Chrome'
# caps['deviceName'] = 'Nexus 6P'
# caps['platformVersion'] = '7.0'
# caps['platformName'] = 'Android'
# caps['deviceOrientation'] = 'portrait'


class DriverConfig:
    cross_browser_config = [('chrome', '', 'ANY'),
                            ('firefox', '', 'ANY')]
    hub = 'http://10.206.8.31:4444/wd/hub'

    @classmethod
    def get_driver_list(cls):
        drivers = []
        for node in cls.cross_browser_config:
            driver_name = node[0] + '-' + node[1] + '-' + node[2]
            drivers.append(driver_name)
        return drivers

    @classmethod
    def get_driver_config(cls, config):
        config = config.split('-')
        browser = config[0]
        if browser.lower() == 'firefox':
            desired_capabilities = DesiredCapabilities.FIREFOX.copy()
            driver = webdriver.Firefox
            executable_path = os.path.join(DRIVER_PATH, 'geckodriver.exe')
        elif browser.lower() == 'chrome':
            if config[2].lower() in ['any', 'vista', 'windows']:
                desired_capabilities = DesiredCapabilities.CHROME.copy()
                driver = webdriver.Chrome
                executable_path = os.path.join(DRIVER_PATH, 'chromedriver.exe')
            else: # Android
                desired_capabilities = DesiredCapabilities.ANDROID.copy()
                desired_capabilities['browserName'] = 'chrome'
                desired_capabilities["platform"] = "Android"
                driver = None
                executable_path = ''
        elif browser.lower() == 'ie':
            desired_capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
            driver = webdriver.Ie
            executable_path = os.path.join(DRIVER_PATH, 'IEDriverServer.exe')
        else:
            desired_capabilities = {}
            driver = None
            executable_path = ''
        desired_capabilities['version'] = config[1]
        desired_capabilities['platform'] = config[2]
        # return cls.get_remote_webdriver(desired_capabilities)
        return cls.get_local_driver(driver, executable_path)

    @classmethod
    def get_local_driver(cls, driver, executable_path):
        return driver(executable_path=executable_path)

    @classmethod
    def get_remote_webdriver(cls, desired_capabilities):
        print("\n starting %s" % desired_capabilities["browserName"])
        return webdriver.Remote(command_executor=cls.hub, desired_capabilities=desired_capabilities)


def generate_configuration(browsers=browsers, platforms=platforms, ie_versions=ie_versions,
                           firefox_versions=firefox_versions, chrome_versions=chrome_versions):
    test_config = []
    for platform in platforms:
        for browser in browsers:
            if browser.lower() == "chrome":
                if not chrome_versions:
                    test_config.append((browser, '', platform))
                    continue
                for chrome_version in chrome_versions:
                    test_config.append((browser, chrome_version, platform))
            elif browser.lower() == "firefox":
                if not firefox_versions:
                    test_config.append((browser, '', platform))
                    continue
                for firefox_version in firefox_versions:
                    test_config.append((browser, firefox_version, platform))
            elif browser.lower() == "ie" and platform.lower() in ['windows', 'xp', 'vista']:
                for ie_version in ie_versions:
                    test_config.append((browser, ie_version, platform))
    return test_config
