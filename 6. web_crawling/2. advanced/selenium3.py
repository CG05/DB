from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.naver.com')

r = driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(5)