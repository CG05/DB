from selenium import webdriver
from selenium.webdriver.common.by import By
import time

user = '본인아이디'
passwd = '본인암호'

driver = webdriver.Chrome()

url_login = 'https://itcyber.edueroom.co.kr/login.php'
driver.get(url_login)
print('로그인창에 접근합니다.')

e = driver.find_element(By.ID, 'userid_id')
e.clear()
e.send_keys(user)
e = driver.find_element(By.ID, 'passwd_id')
e.clear()
e.send_keys(passwd)

time.sleep(3)

form = driver.find_element(By.CSS_SELECTOR, 'input.mlogin_btn[type=submit]')
form.submit()
print('로그인 버튼을 클릭합니다.')

time.sleep(5)
driver.get('https://itcyber.edueroom.co.kr/order.php?action=cart')

shopping = driver.find_elements(By.CSS_SELECTOR, 'tbody > tr > td.ta_l > a')
# print(shopping)

for s in shopping:
    print("-", s.text)