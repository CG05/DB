import urllib.request
import urllib.parse

# 날씨 API로 정보 받아오기 
# 중기 날씨 
API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

# stnId : 지역 지정 매개 변수
# 전국 : 108, 서울/경기 : 109, 강원도 : 105, ....
# 교재 참조

values = {
    'stnId' : '108'
}

# urllib.parse.urlencode : 값들의 기호나 한글을 encoding 
params = urllib.parse.urlencode(values)
url = API + "?" + params

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)