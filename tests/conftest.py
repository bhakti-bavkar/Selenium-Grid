from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import pytest
from CommonLib import browser_platform_conf

@pytest.fixture(scope='module')
def local_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    return webdriver.Firefox(executable_path='C:\Program Files (x86)\Python36-32\drivers\geckodriver.exe',firefox_options=options)

@pytest.fixture(scope='module')
def grid_driver():
    nodeURL = "http://10.206.8.69:5566/wd/hub"
    return webdriver.Remote(command_executor=nodeURL, desired_capabilities=DesiredCapabilities.FIREFOX)


@pytest.fixture(scope='module')
def browser():
    return pytest.config.getoption("-B")


# @pytest.fixture(scope='module')
# def browserstack_flag():
#     return pytest.config.getoption("-M")


@pytest.fixture(scope='module')
def browser_version():
    return pytest.config.getoption("-V")


@pytest.fixture(scope='module')
def platform():
    return pytest.config.getoption("-P")


@pytest.fixture(scope='module')
def os_version():
    return pytest.config.getoption("-O")


def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     action="append",
                     default=[],
                     help="Browser. Valid options are firefox, ie and chrome")
    # parser.addoption("-M", "--browserstack_flag",
    #                  dest="browserstack_flag",
    #                  default="N",
    #                  help="Run the test in Browserstack: Y or N")
    parser.addoption("-O", "--os_version",
                     dest="os_version",
                     action="append",
                     help="The operating system: xp, 7",
                     default=[])
    parser.addoption("-V", "--ver",
                     dest="browser_version",
                     action="append",
                     help="The version of the browser: a whole number",
                     default=[])
    parser.addoption("-P", "--platform",
                     dest="platform",
                     action="append",
                     help="The operating system: Windows 7, Linux",
                     default=[])

def pytest_generate_tests(metafunc):
    if 'browser' in metafunc.fixturenames:
        #if metafunc.config.getoption("-M").lower() == 'y':
        if metafunc.config.getoption("-B") == ["all"]:
            metafunc.parametrize("browser,browser_version,platform,os_version",
                                 browser_platform_conf.cross_browser_cross_platform_config)

def pytest_funcarg__driverconfig(request): # factory function
    return DriverConfig(request)

class DriverConfig:
    def __init__(self,request):
        self.config = request.config

    def get_webdriver(self):
        browser = self.config.option.browser
        if browser.lower() == 'firefox':
            desired_capabilities = DesiredCapabilities.FIREFOX
        elif browser.lower() == 'chrome':
            desired_capabilities = DesiredCapabilities.CHROME

        desired_capabilities['os'] = platform
        desired_capabilities['os_version'] = os_version
        desired_capabilities['browser_version'] = browser_version

        return webdriver.Remote(command_executor='', desired_capabilities=desired_capabilities)


def get_webdriver(browser, browser_version, platform, os_version):
    #"Run the test in browser stack browser stack flag is 'Y'"
    # USERNAME = user_name  # We fetch values from a conf file in our framework we use on our clients
    # PASSWORD = access_key
    if browser.lower() == 'firefox':
        desired_capabilities = DesiredCapabilities.FIREFOX
    if browser.lower() == 'chrome':
        desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities['os'] = platform
    desired_capabilities['os_version'] = os_version
    desired_capabilities['browser_version'] = browser_version

    return webdriver.Remote(command_executor='', desired_capabilities=desired_capabilities)