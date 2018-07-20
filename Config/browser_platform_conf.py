from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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
cross_browser_config = [('chrome', '', 'ANDROID')]


def get_driver_config():
    nodes = cross_browser_config
    remote_drivers = {}
    for node in nodes:
        browser = node[0]
        if browser.lower() == 'firefox':
            desired_capabilities = DesiredCapabilities.FIREFOX.copy()
            # driver = webdriver.Firefox
            # executable_path = 'C:\Program Files (x86)\Python36-32\drivers\geckodriver.exe'
        elif browser.lower() == 'chrome':
            if node[2].lower() in ['any', 'vista', 'windows']:
                desired_capabilities = DesiredCapabilities.CHROME.copy()
                # driver = webdriver.Chrome
                # executable_path = 'C:\Program Files (x86)\Python36-32\drivers\chromedriver.exe'
            else: # Android
                desired_capabilities = DesiredCapabilities.ANDROID.copy()
                desired_capabilities['browserName'] = 'chrome'
                desired_capabilities["platform"] = "Android"
        elif browser.lower() == 'ie':
            desired_capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
            driver = webdriver.Ie
            executable_path = 'C:\Program Files (x86)\Python36-32\drivers\IEDriverServer.exe'
        else:
            desired_capabilities = {}
            driver = None
            executable_path = ''
        desired_capabilities['version'] = node[1]
        desired_capabilities['platform'] = node[2]
        driver_name = node[0] + '_' + node[1] + '_' + node[2]
        remote_drivers[driver_name] = get_remote_webdriver(desired_capabilities)
        # remote_drivers[driver_name] = get_local_driver(driver, executable_path)
    return remote_drivers


def get_local_driver(driver, executable_path):
    return driver(executable_path=executable_path)


def get_remote_webdriver(desired_capabilities):
    nodeURL = 'http://10.206.8.31:4444/wd/hub'
    print("\n starting %s" % desired_capabilities["browserName"])
    return webdriver.Remote(command_executor=nodeURL, desired_capabilities=desired_capabilities)


cross_browser_drivers = get_driver_config()


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
