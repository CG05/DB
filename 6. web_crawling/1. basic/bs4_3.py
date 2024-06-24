from bs4 import BeautifulSoup
import urllib.request

html = '''
<html>
    <head>
        <title>연습</title>
    </head>
    <body>
        <h1 id='title'>연습입니다.</h1>
        <p id='body'>스크레이핑이란</p>
        <p>원하는 부분을 추출하는 것입니다.</p>
    </body>
</html>
'''
soup = BeautifulSoup(html, 'html.parser')

# 아이디 요소 찾는 법
title = soup.find(id='title')
body = soup.find(id='body')

print(f'#title : {title.string}')
print(f'#body : {body.string}')