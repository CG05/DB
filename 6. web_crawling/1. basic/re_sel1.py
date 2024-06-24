from bs4 import BeautifulSoup
import re

fp = open(r'6. web_crawling\1. basic\re_sel.html', 'r', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

# find : 요소와 요소의 속성으로 찾는다.
li = soup.find_all(href=re.compile(r'^https://'))

for l in li:
    print(l)
    print(l.attrs['href'])