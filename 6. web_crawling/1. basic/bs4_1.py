from bs4 import BeautifulSoup
import urllib.request

html = '''
<html>
    <head>
        <title>연습</title>
    </head>
    <body>
        <h1>연습입니다.</h1>
        <p>스크레이핑이란</p>
        <p>원하는 부분을 추출하는 것입니다.</p>
    </body>
</html>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup)
print("=" * 50)
print(soup.html)
print("=" * 50)
print(soup.html.body)
print("=" * 50)
print(soup.html.body.h1)
print("=" * 50)
print(soup.html.body.p)
print("=" * 50)
print(soup.html.body.p.next_sibling.next_sibling)