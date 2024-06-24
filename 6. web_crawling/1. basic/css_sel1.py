from bs4 import BeautifulSoup

fp = open(r'6. web_crawling\1. basic\test.html', 'r', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

sel = lambda x : print(soup.select_one(x).string)
sel('#nu')
sel('li#nu')
sel('ul #nu')
sel('ul > li#nu')
sel('#bible > #nu')
sel('ul#bible > li#nu')
sel('li[id="nu"]')
sel('li:nth-of-type(4)')
sel('li:nth-child(4)')
sel('li:nth-last-child(2)')

print(soup.select('li')[3].string)
print(soup.find_all('li')[3].string)