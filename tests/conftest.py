import pytest
from Config.browser_platform_conf import DriverConfig


def pytest_generate_tests(metafunc):
    drivers = DriverConfig.get_driver_list()
    if 'driver' in metafunc.fixturenames:
            metafunc.parametrize('driver', drivers, indirect=True)


@pytest.fixture(scope='class')
def driver(request):
    try:
        web_driver = DriverConfig.get_remote_driver_config(request.param)
        if request.cls is not None:
            request.cls.driver = web_driver
        request.addfinalizer(web_driver.close)
        return web_driver
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

