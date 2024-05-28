import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = {
    "browserName": "chrome",
    "browserVersion": "109",
    "enableVNC": True
    }


chrome_options = webdriver.ChromeOptions()
# chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                          options=chrome_options,
                          desired_capabilities=capabilities)

driver.get("https://selenium.dev")
driver.find_element_by_css_selector('div.card-footer a[href="/documentation/webdriver/"]').click()
time.sleep(120)
