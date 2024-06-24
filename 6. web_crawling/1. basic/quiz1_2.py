import urllib.request
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/exchangeList.naver'
res = urllib.request.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

country = soup.select("td.tit")
values = soup.select("td.sale")

import re 

for c,v in zip(country, values):
    c = re.sub(r"\s+", "", c.string)
    print(f'{c} : {v.string}')

    with open(r'd:\finance.txt', 'a+', encoding='utf-8') as f:
        f.write(f'{c} : {v.string}\n')