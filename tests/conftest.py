import pytest
from Config.browser_platform_conf import DriverConfig


def pytest_load_initial_conftests(args):
    if "xdist" in sys.modules:  # pytest-xdist plugin
        import multiprocessing
        num = max(multiprocessing.cpu_count() / 2, 1)
        args[:] = ["-n", str(num)] + args


# @pytest.fixture(scope='session')
# def get_driver(request):
#     session = request.node
#     web_drivers = get_driver_config()
#     for item in session.items:
#         cls = item.getparent(pytest.Class)
#         setattr(cls.obj,"driver",web_drivers)
#     yield

def pytest_generate_tests(metafunc):
    drivers = DriverConfig.get_driver_list()
    if 'driver' in metafunc.fixturenames:
            metafunc.parametrize('driver', drivers, indirect=True)


@pytest.fixture()
def driver(request):
    try:
        web_driver = DriverConfig.get_driver_config(request.param)
        if request.cls is not None:
            request.cls.driver = web_driver
        request.addfinalizer(web_driver.close)
    except Exception:
        print('Driver with given parameter not found')


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
