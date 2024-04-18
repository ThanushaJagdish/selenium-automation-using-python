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

    driver.close()
    #it closes current tab only
    #session id is not null

    time.sleep(20)