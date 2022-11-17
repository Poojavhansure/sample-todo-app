from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json

url = os.getenv("LT_HUB_URL")
capabilities = [
    {
        "browserName": "Chrome",
        "browserVersion": "103.0",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python sample parallel",  # test name
        "buildName": LT_BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "Firefox",
        "browserVersion": "102.0",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "BStack Python sample parallel",
        "buildName": LT_BUILD_NAME,
    },
    {
        "browserName": "Safari",
        "browserVersion": "14.1",
        "os": "OS X",
        "osVersion": "Big Sur",
        "sessionName": "BStack Python sample parallel",
        "buildName": LT_BUILD_NAME,
    },
]
driver = webdriver.Remote(
    desired_capabilities= capabilities,
    command_executor= url
)
driver.get("http://localhost:8081/")
driver.find_element_by_name("li3").click()

textbox = driver.find_element_by_id("sampletodotext")
textbox.send_keys("Testing")
driver.find_element_by_id("addbutton").click()
assert "No results found." not in driver.page_source
driver.execute_script("lambda-status=passed")
driver.quit()
