import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URl_OpenCart_Register_Account="https://awesomeqa.com/ui/index.php?route=account/register"

def test_URl_OpenCart_Register_Account():
    driver=webdriver.Chrome()
    driver.get(URl_OpenCart_Register_Account)
    time.sleep(5)
    driver.find_element(By.ID,"input-firstname").send_keys("ASHU")
    driver.find_element(By.ID ,"input-lastname").send_keys("KUMAR")
    driver.find_element(By.ID ,"input-email").send_keys("kuyqu44@gmail.com")
    driver.find_element(By.ID ,"input-telephone").send_keys("7707073263")
    driver.find_element(By.ID ,"input-password").send_keys("7707073263")
    driver.find_element(By.ID ,"input-confirm").send_keys("7707073263")
    ## Check Box agree.
    driver.find_element(By.NAME, "agree").click()
    time.sleep(5)
    #Continue
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    time.sleep(3)
    #btn_continue = driver.find_element(By.XPATH, "//*[@type='submit']")
    #btn_continue.click()
    #Verfiations
    message=driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/h1[1]").text
    time.sleep(1)
    print(message)
   # assert message=="Your Account Has Been Created!"
    assert message.__eq__("Your Account Has Been Created!")





   
