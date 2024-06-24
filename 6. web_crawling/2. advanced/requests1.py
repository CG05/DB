import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

id = '본인 아이디'
pwd = '본인 암호'

session = requests.session()

login_info = {
    'm_id' : id,
    'm_passwd' : pwd
}

url_login = 'https://www.hanbit.co.kr/member/login_proc.php'
res = session.post(url_login, data=login_info)
res.raise_for_status()

url_shopping = 'https://www.hanbit.co.kr/myhanbit/myhanbit.html'
res = session.get(url_shopping)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
mileage = soup.select_one('.mileage_section1 span').get_text()
ecoin = soup.select_one('.mileage_section2 span').get_text()

print("마일리지 : ", mileage)
print('한빛코인 : ', ecoin)