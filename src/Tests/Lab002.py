from selenium import webdriver


def test_open_vwo_login():
    driver = webdriver.Chrome()
    # Post Request to Create a New Fresh copy of chrome
    driver.get("https://app.vwo.com")
    print(driver.title)  # Get Request
    assert driver.title == "Login - VWO"
