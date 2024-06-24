import urllib.request
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'

response = urllib.request.urlopen(url)
data = response.read()

# response  header에서 encoding
encoding = response.headers.get_content_charset(failobj='utf-8')
text_data = data.decode(encoding)

soup = BeautifulSoup(text_data, 'html.parser')
country = soup.select("h3.h_lst")
values = soup.select("div.head_info > span.value")
currents = soup.select("div.head_info > span > span.blind")

for c,v,cu in zip(country,values, currents):
    print(f'{c.string} : {v.string} {cu.string}')
