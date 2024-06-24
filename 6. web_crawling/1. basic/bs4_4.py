from bs4 import BeautifulSoup

html = '''
<html>
    <head>
        <title>여러요소 가져오기</title>
    </head>
    <body>
        <a href='https://www.google.com'>구글</a>
        <a href='https://www.naver.com'>네이버</a>
        <a href='https://www.daum.net'>다음</a>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')

for link in links:
    url = link.attrs['href']
    url_name = link.string
    print(f'{url_name} : {url} ')