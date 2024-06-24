import urllib.request
import urllib.parse
import sys 

API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

if len(sys.argv) <= 1:
    print("파라미터를 입력해주세요.")
    sys.exit()

region = sys.argv[1]

values = {
    'stnId' : region
}

# urllib.parse.urlencode : 값들의 기호나 한글을 encoding 
params = urllib.parse.urlencode(values)
url = API + "?" + params

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)