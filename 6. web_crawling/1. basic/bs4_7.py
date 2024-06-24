# CSS 선택자
# ul > li > a > img
from bs4 import BeautifulSoup

html = '''
<body>
    <div id='first'>
        <h1>가수 리스트</h1>
        <ul class='singer'>
            <li>에스파</li>
            <li>뉴진스</li>
            <li>아일릿</li>
        </ul>
    </div>
    <div id='main'>
        <h1>게임 리스트</h1>
        <ul class='games'>
            <li>LOL</li>
            <li>Starcraft</li>
            <li>WOW</li>
        </ul>
    </div>
</body>
'''

soup = BeautifulSoup(html, 'html.parser')

# BeautifulSoup.select_one() : 선택된 하나의 요소만 가져오기
# BeautifulSoup.select() : 선택된 요소 여러개를 가져오기
print(soup.select_one("div#main > h1"))
print(soup.select_one("div#main > ul"))
print(soup.select_one("div > ul.games"))
print(soup.select('div#main > ul > li'))
print(soup.select('div > ul.games > li'))
print(soup.select('div#main > ul.games > li'))
