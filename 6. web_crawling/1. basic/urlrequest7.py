import urllib.request
import urllib.parse
import sys 

API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

if len(sys.argv) <= 1:
    print("지역을 입력해주세요.")
    sys.exit()

region_code = {'전국':'108', '서울':'109', '경기':'109', '강원도':105,
               '충청북도':'131', '충청남도':'133','전라북도':'146','전라남도':'156',
               '경상북도':'143', '경상남도':'159', '제주도':'184'} 

region = sys.argv[1]

if region_code.get(region):
    values = {
        'stnId' : region_code.get(region)
    }

    # urllib.parse.urlencode : 값들의 기호나 한글을 encoding 
    params = urllib.parse.urlencode(values)
    url = API + "?" + params

    data = urllib.request.urlopen(url).read()
    text = data.decode('utf-8')
    print(text)
else :
    print("없는 지역 입니다.")

# 기상청 자료 개방 포털
# https://data.kma.go.kr/tmeta/stn/selectStnList.do

'''
기상청 행정코드(지역코드) api
시도코드 : http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt
구군코드 : http://www.kma.go.kr/DFSROOT/POINT/DATA/mdl.11.json.txt
읍면동코드 : http://www.kma.go.kr/DFSROOT/POINT/DATA/leaf.11110.json.txt
'''