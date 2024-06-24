from selenium import webdriver

url = 'http://www.naver.com'

driver = webdriver.Chrome()
driver.get(url)
driver.save_screenshot("naver.png")
driver.quit()