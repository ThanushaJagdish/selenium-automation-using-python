import time

from selenium import webdriver
import pytest
import allure_pytest
from selenium.webdriver.common.by import By


@pytest.mark.test_make_appointment_element_of_herokuapp
def test_open_website():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")
    #find the element of make booking button
    #<a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>
    # here id is unique in the websites html structure
    element=driver.find_element(By.ID,value="btn-make-appointment")
    element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    #<div class="col-sm-12 text-center">
    #<h2>Login</h2>
    #<p class="lead">Please login to make appointment.</p>
    #</div>

    login_page_element = driver.find_element(By.TAG_NAME,"p")
    assert login_page_element.text == "Please login to make appointment."
    time.sleep(2)

    #<input
    # type="text"
    # class="form-control"
    # id="txt-username"
    # name="username"
    # placeholder="Username"
    # value="" autocomplete="off">

    username_element = driver.find_element(By.ID,"txt-username")
    username_element.send_keys("John Doe")
    time.sleep(2)

    #<input
    # type="password"
    # class="form-control"
    # id="txt-password"
    # name="password"
    # placeholder="Password"
    # value="" autocomplete="off">

    password_element = driver.find_element(By.ID,"txt-password")
    password_element.send_keys("ThisIsNotAPassword")
    time.sleep(2)

    #<button
    # id="btn-login"
    # type="submit"
    # class="btn btn-default">Login</button>

    submit_element=driver.find_element(By.ID,"btn-login")
    submit_element.click()
    time.sleep(2)

    #<div class="col-sm-12 text-center">
    #<h2>Make Appointment</h2>
    #<hr class="small">
    #</div>

    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/#appointment"

    appointment_page_element = driver.find_element(By.TAG_NAME,"h2")
    assert appointment_page_element.text=="Make Appointment"
    time.sleep(2)




