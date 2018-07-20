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


capabilities = [{

}]

cross_browser_cross_platform_config = [('chrome', '', 'ANY'),('firefox', '', 'ANY')]
