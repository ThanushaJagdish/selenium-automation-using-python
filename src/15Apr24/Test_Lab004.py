import time

from selenium import webdriver
import pytest
import allure_pytest

#driver_path="xyz"
#driver = webdriver.EdgeService(executable_path=driver_path)
#driver.get("http")
@pytest.mark.test
def test_open_website():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com")

    driver.maximize_window()
    assert driver.title=="Login - VWO"

    driver.quit()
    #it closes all the tabs
    #session id is set to null

    time.sleep(20)