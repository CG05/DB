import requests
import json

apikey = '7ddd4558a0f238817f5989a230bae8ef'
apiurl = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

cities = ['Seoul,KR', 'Tokyo,JP', 'New York,US']

# 절대온도
k2c = lambda k : k - 273.15

for name in cities:
    url = apiurl.format(city=name, key=apikey)
    r = requests.get(url)
    data = json.loads(r.text)

    print("+ 도시 =", data['name'])
    print("| 날씨 =", data['weather'][0]['description'])
    print("| 최저 기온 =", k2c(data['main']['temp_min']))
    print("| 최고 기온 =", k2c(data['main']['temp_max']))
    print("| 습도 =", data['main']['humidity'])
    print("| 기압 =", data['main']['pressure'])
    print("| 풍향 =", data['wind']['deg'])
    print("| 풍속 =", data['wind']['speed'])
    print()

    with open('weather.txt', 'a+', encoding='utf-8') as f:
        f.write(str(data))
        f.write("\n\n")