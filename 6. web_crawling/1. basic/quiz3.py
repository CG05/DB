# a 태그를 가져와서 텍스트와 url을 출력해 보세요
from bs4 import BeautifulSoup
import urllib.request as req
import re

url = 'https://entertain.naver.com/home'
res = req.urlopen(url)

# print(res.getcode())

soup = BeautifulSoup(res, 'html.parser')

# a_tag = soup.find_all(href=re.compile(r'^https://'))
a_tag = soup.select('a[href^=https]')

for a in a_tag:
    if a.string != None:
        a_text = re.sub(r"\t|\n", "", a.string)
        print(f'{a_text}')
        print(a.attrs['href'])
