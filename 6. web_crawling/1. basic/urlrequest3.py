import urllib.request

url = 'https://www.google.com'

result = urllib.request.urlopen(url)
# <http.client.HTTPResponse object at 0x000002652467F760> : Response 를 받았다.
# HTTPResponse 객체

# HTTPResponse.read() : response 로 받은 값을 읽어온다.
data = result.read()

text = data.decode('utf-8')
print(text)

