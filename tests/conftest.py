from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import pytest
from Config import browser_platform_conf
import sys
from threading import Thread


# def pytest_load_initial_conftests(args):
#     if "xdist" in sys.modules:  # pytest-xdist plugin
#         import multiprocessing
#
#         num = max(multiprocessing.cpu_count() / 2, 1)
#         args[:] = ["-n", str(num)] + args

@pytest.fixture(scope='session')
def local_driver():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Firefox(executable_path='C:\Program Files (x86)\Python36-32\drivers\geckodriver.exe',firefox_options=options)

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
    nodes = browser_platform_conf.cross_browser_cross_platform_config
    remote_drivers = []
    for node in nodes:
        browser = node[0]
        if browser.lower() == 'firefox':
            desired_capabilities = DesiredCapabilities.FIREFOX.copy()
        elif browser.lower() == 'chrome':
            desired_capabilities = DesiredCapabilities.CHROME.copy()
        elif browser.lower() == 'ie':
            desired_capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
        elif browser.lower() == 'edge':
            desired_capabilities = DesiredCapabilities.EDGE.copy()
        elif browser.lower() == 'android':
            desired_capabilities = DesiredCapabilities.ANDROID.copy()
        elif browser.lower() == 'iphone':
            desired_capabilities = DesiredCapabilities.IPHONE.copy()
        else:
            break
        desired_capabilities['platform'] = node[2]
        desired_capabilities['os_version'] = node[3]
        desired_capabilities['version'] = node[1]
        remote_drivers.append(get_webdriver(desired_capabilities))
    metafunc.parametrize('driver', remote_drivers)

def get_webdriver(desired_capabilities):
    nodeURL = 'http://localhost:4444/wd/hub'
    print("starting %s\n" % desired_capabilities["browserName"])
    return webdriver.Remote(command_executor=nodeURL, desired_capabilities=desired_capabilities)

# def pytest_funcarg__driverconfig(request): # factory function
#     driver = DriverConfig(request)

class DriverConfig:
    def __init__(self,request):
        self.config = browser_platform_conf.cross_browser_cross_platform_config

    # def init_webdriver(self):
    #     threads = []
    #     for node in self.config:
    #         browser = node[0]
    #         if browser.lower() == 'firefox':
    #             desired_capabilities = DesiredCapabilities.FIREFOX
    #         elif browser.lower() == 'chrome':
    #             desired_capabilities = DesiredCapabilities.CHROME
    #         desired_capabilities['os'] = node[2]
    #         desired_capabilities['os_version'] = node[3]
    #         desired_capabilities['browser_version'] = node[1]
    #         thread = Thread(target=get_webdriver, args=[desired_capabilities])
    #         threads.append(thread)
    #         thread.start()
    #     for thread in threads:
    #         thread.join()

