from selenium import webdriver

def test_nyt_homepage_loads():
    driver = webdriver.Chrome()
    driver.get("https://www.msnbc.com/")
    driver.get_screenshot_as_file('artifacts/screenshots/basic-screenshot-artifact-msnbc.png')
    driver.quit()
