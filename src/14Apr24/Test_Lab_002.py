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
    print(driver.title)
    print(driver.page_source)
    driver.maximize_window()
    assert driver.title=="Login - VWO"
