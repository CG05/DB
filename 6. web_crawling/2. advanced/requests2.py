import requests

r = requests.get('http://www.google.com')

print("google : ", r)
formdata = {'key1':'value1', 'key2':'value2'}
r = requests.post('http://example.com', data=formdata)
print('exmaple.com :', r)

# get : select - 데이터 가져오기
# post : insert - 데이터 입력(저장)하기
# put : update - 데이터 수정하기
# delete : delete - 데이터 삭제하기
r = requests.put('http://httpbin.org/put')
print("put :, ", r)
r = requests.delete('http://httpbin.org/delete')
print('delete :', r)
r = requests.head('http://httpbin.org/head')
print('head : ', r)

r = requests.get('http://api.aoikujira.com/time/get.php')

text = r.text
print(text)
bin = r.content
print(bin)

r = requests.get('https://wikibook.co.kr/logo.png')

with open('wiki.png', 'wb') as f:
    f.write(r.content)

print('saved')