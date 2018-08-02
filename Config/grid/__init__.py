# hub
# java -jar selenium-server-standalone-3.13.0.jar -role hub -hubConfig "hub.json"
# node_1
# java -Dwebdriver.gecko.driver="../../../../drivers/geckodriver.exe" -Dwebdriver.chrome.driver="../../../../drivers/chromedriver.exe" -jar selenium-server-standalone-3.13.0.jar -role node -nodeConfig "../nodes/node_1.json"
# node_2
# java -Dwebdriver.gecko.driver="../../../../drivers/geckodriver.exe" -Dwebdriver.chrome.driver="../../../../drivers/chromedriver.exe" -jar selenium-server-standalone-3.13.0.jar -role node -nodeConfig "../nodes/node_2.json"

# node_3
# java -Dwebdriver.ie.driver="../../../../drivers/IEDriverServer.exe" -jar selenium-server-standalone-3.13.0.jar -role node -nodeConfig "../nodes/node_3.json"

# To shutdown
# wget http://localhost:4444/selenium-server/driver/?cmd=shutDownSeleniumServer


