from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json

url = os.getenv("LT_HUB_URL")
capabilities = {
    options = ChromeOptions()
    options.browser_version = "108.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = "poojarani";
    lt_options["accessKey"] = "dgj3OUvt0nfuMhh5XiDONY23IzlkfKSsl2rb2PWEp80k4lxO55";
    lt_options["project"] = "Untitled";
    lt_options["w3c"] = True;
    lt_options["plugin"] = "python-python";
    options.set_capability('LT:Options', lt_options);
}
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
