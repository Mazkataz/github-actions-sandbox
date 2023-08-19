from selenium import webdriver

def test_nyt_homepage_loads():
    driver = webdriver.Chrome()
    driver.get("https://www.nytimes.com/")
    print(driver.title())
    driver.get_screenshot_as_file('artifacts/screenshots/basic-screenshot-artifact-nyt.png')
    driver.quit()
