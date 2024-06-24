from bs4 import BeautifulSoup

fp = open(r'6. web_crawling\1. basic\quiz.html', 'r', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

# select : css 형식의 선택자
# yellow = soup.select(".yellow")
yellow = soup.select('ul > li.yellow')
# find : 태그 형식의 선택자
# yellow = soup.find_all('.yellow')

print("노란색 과일")
for y in yellow:
    print(f'- {y.string}')

us = soup.select('li[data-lo="us"]')
print("미국산 과일과 야채")
for u in us:
    print(f'- {u.string}')

green = soup.select('.green')
print("초록색 과일과 야채")
for g in green:
    print(f'- {g.string}')

green_ve = soup.select('ul#ve-list > li.green')
print("초록색 야채")
for g in green_ve:
    print(f'- {g.string}')

kr = soup.select('li[data-lo="kr"]')
print("국산 과일과 야채")
for k in kr:
    print(f'- {k.string}')