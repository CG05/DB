import urllib.request

# url = 'https://finance.naver.com/marketindex/'
url = 'https://news.naver.com/section/102'

try:
    response = urllib.request.urlopen(url)
    print(response.getcode()) # 200, 300 크롤링 가능
except urllib.error.HTTPError as e:
    print(e.code) # 400대, 500대 크롤링 불가능