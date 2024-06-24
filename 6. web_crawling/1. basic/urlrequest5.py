import urllib.request
import urllib.parse

API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

region = input('지역 번호 입력 : ')

values = {
    'stnId' : region
}

# urllib.parse.urlencode : 값들의 기호나 한글을 encoding 
params = urllib.parse.urlencode(values)
url = API + "?" + params

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)