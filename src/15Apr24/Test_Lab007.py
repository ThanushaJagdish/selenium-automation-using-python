import time

from selenium import webdriver
import pytest
import allure_pytest
from selenium.webdriver.common.by import By


@pytest.mark.app_vwo_login
def test_open_website():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com")

    #<input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi">

    #id->name->class->tag->linktext->partialtext->css selector->xpath

    email_element=driver.find_element(By.NAME,"username")
    email_element.send_keys("admin")
    time.sleep(2)

    #<input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe">

    password_element = driver.find_element(By.ID, "login-password")
    password_element.send_keys("admin")
    time.sleep(2)

    #<button
    # type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica">
	#<span class="icon loader hidden"
    # data-qa="zuyezasugu"></span>
	#<span data-qa="ezazsuguuy">Sign in</span>
	#</button>

    sign_in_element = driver.find_element(By.ID,"js-login-btn")
    sign_in_element.click()
    time.sleep(2)

    #<div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">Your email, password, IP address or location did not match</div>

    error_msg_element=driver.find_element(By.ID,"js-notification-box-msg")
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    time.sleep(2)

