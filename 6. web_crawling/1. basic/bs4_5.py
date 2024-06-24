from bs4 import BeautifulSoup

html = '''
<body>
    <ul>
        <li><a href='test.html' target='_blank' title='test페이지로 이동'>test</a></li>
    </ul>
</body>
'''

soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# print(soup.prettify())

a = soup.a
print(a)
print(a.attrs)

for key, value in a.attrs.items():
    print(f'{key} : {value}')