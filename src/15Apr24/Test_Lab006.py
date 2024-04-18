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
    time.sleep(5)
