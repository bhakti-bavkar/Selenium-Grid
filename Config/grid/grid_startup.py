import os, json, requests
from Config import CONFIG_PATH, DRIVER_PATH


class GridSetup:    
    base_path = os.path.join(CONFIG_PATH,'grid\jars')
    server_path = os.path.join(base_path,'server')
    node_path = os.path.join(base_path,'nodes')
    grid_jar  = "\\selenium-server-standalone-3.13.0.jar"

    @classmethod
    def start_hub(cls):
        cmd = "java -jar " + cls.server_path + cls.grid_jar\
              + " -role hub -hubConfig " + cls.server_path + '\\hub.json'
        os.system(cmd)

    @classmethod
    def start_node(cls, node_config_file):
        browsers = []
        cmd = 'java '
        node_config_file = cls.node_path + node_config_file
        with open(node_config_file) as f:
            node = json.load(f)

        for cap in node["capabilities"]:
            if cap["maxInstances"] == 0:
                continue
            if cap["browserName"] == "firefox":
                driver_path = DRIVER_PATH + "\\geckodriver.exe"
                browsers.append(" -Dwebdriver.gecko.driver=" + driver_path)
            elif cap["browserName"] == "chrome":
                driver_path = DRIVER_PATH + "\\chromedriver.exe"
                browsers.append(" -Dwebdriver.chrome.driver=" + driver_path)
            elif cap["browserName"] == "internet explorer":
                driver_path = DRIVER_PATH + "\\safari.exe"
                browsers.append(" -Dwebdriver.safari.driver=" + driver_path)

        for browser in browsers:
            cmd += browser

        cmd += " -jar " + cls.server_path + cls.grid_jar
        cmd += " -role node -nodeConfig " + node_config_file
        os.system(cmd)

    @classmethod
    def close_hub(cls):
        url = 'http://localhost:4444/selenium-server/driver/?cmd=shutDownSeleniumServer'
        requests.post(url)


