from asyncio import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

"""Open the URl - https://katalon-demo-cura.herokuapp.com/
Find and Click on the Make Appointment button
Verify the URL
On the Next Page 
Find and Enter the details of the username and password ( web_element.send_keys()
Click on the Submit button (click()
Verify the URL change."""


def test_Task_17OCT():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")
    Make_Appointment = driver.find_element(By.ID, "btn-make-appointment")
    Make_Appointment.click()
    verify = driver.current_url
    assert verify == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    # Login
    user_name = driver.find_element(By.ID, "txt-username")
    user_name.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    Login_button = driver.find_element(By.ID, "btn-login")
    Login_button.click()
    cuurent = driver.current_url
    assert cuurent == "https://katalon-demo-cura.herokuapp.com/#appointment"
    sleep(10)
