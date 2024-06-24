import urllib.request

url = 'https://cdn.hankyung.com/photo/202403/01.36047379.1.jpg'
savename = '6. web_crawling/1. basic/download/karina.png'

urllib.request.urlretrieve(url, savename)
print('저장완료')