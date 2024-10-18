import selenium
from selenium import webdriver


def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/Alert.html")
    alert = driver.switch_to.alert

    print("Alert text:", alert.text)

    alert.accept()
