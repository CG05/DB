import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, 'html.parser')
# print(soup.title.string)

# BeautifulSoup.find() : 해당하는 요소를 하나 가지고 온다.
title = soup.find('title').string
wf = soup.find('wf').string
print(title)
print(wf)