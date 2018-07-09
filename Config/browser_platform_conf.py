browsers = ["chrome", "firefox"]#, "IE"]
os_list = ["windows"]#, "OS X"]
chrome_versions = ["67"]#, "50"]
firefox_versions = ["61"]
windows_versions = ["VISTA"]#, "8.1"]
os_x_versions = []


def generate_configuration(browsers=browsers, firefox_versions=firefox_versions, chrome_versions=chrome_versions,
                           os_list=os_list, windows_versions=windows_versions, os_x_versions=os_x_versions):
    test_config = []
    for browser in browsers:
        if browser == "chrome":
            for chrome_version in chrome_versions:
                for os_name in os_list:
                    if os_name == "windows":
                        for windows_version in windows_versions:
                            config = [browser, chrome_version, os_name, windows_version]
                            test_config.append(tuple(config))
                    if os_name == "OS X":
                        for os_x_version in os_x_versions:
                            config = [browser, chrome_version, os_name, os_x_version]
                            test_config.append(tuple(config))
        elif browser == "firefox":
            for firefox_version in firefox_versions:
                for os_name in os_list:
                    if os_name == "windows":
                        for windows_version in windows_versions:
                            config = [browser, firefox_version, os_name, windows_version]
                            test_config.append(tuple(config))
                    if os_name == "OS X":
                        for os_x_version in os_x_versions:
                            config = [browser, firefox_version, os_name, os_x_version]
                            test_config.append(tuple(config))


    return test_config

cross_browser_cross_platform_config = generate_configuration()
