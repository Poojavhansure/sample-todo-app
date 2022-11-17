from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json

url = os.getenv("LT_HUB_URL")
capabilities = {
    ChromeOptions browserOptions = new ChromeOptions();
    browserOptions.setPlatformName("Windows 10");
    browserOptions.setBrowserVersion("108.0");
    HashMap<String, Object> ltOptions = new HashMap<String, Object>();
    ltOptions.put("username", "poojarani");
    ltOptions.put("accessKey", "dgj3OUvt0nfuMhh5XiDONY23IzlkfKSsl2rb2PWEp80k4lxO55");
    ltOptions.put("project", "Untitled");
    ltOptions.put("selenium_version", "4.0.0");
    ltOptions.put("w3c", true);
    browserOptions.setCapabilities("LT:Options", ltOptions);
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
