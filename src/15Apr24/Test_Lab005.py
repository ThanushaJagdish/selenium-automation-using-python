import time

from selenium import webdriver
import pytest
import allure_pytest


@pytest.mark.test
def test_open_website():
    driver=webdriver.Chrome()
    driver.get("https://bing.com/chat")
    time.sleep(9)
    driver.get("https://google.com")
    driver.back()
    time.sleep(9)
    driver.forward()
    time.sleep(9)
    driver.refresh()
    time.sleep(9)

