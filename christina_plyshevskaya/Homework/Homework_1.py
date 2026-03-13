import requests

response = requests.get('https://httpbin.org/json')
response.raise_for_status()
data = response.json()
title = data['slideshow']['title']
print(f'Title: {title}')


import requests

data = {'username': 'test_user', 'password': 'qwerty'}

try:
    response = requests.post('https://httpbin.org/post', data=data)
    response.raise_for_status()
    print(response.json()['form'])

except requests.exceptions.HTTPError as HTTPError:
    print(f'Ошибка: {HTTPError.response.status_code}')

except requests.exceptions.RequestException:
    print('Сервер недоступен:(')


import requests

session = requests.Session()
session.get('https://httpbin.org/cookies/set/test_cookie/12345')
response_cookies = session.get('https://httpbin.org/cookies')
data = response_cookies.json()
cookie_value = data['cookies'].get('test_cookie')

file_content = 'текстовый файл через POST'
file_name = 'test_cookies.txt'
with open(file_name, 'w', encoding='utf-8') as f:
    f.write(file_content)
file_size = len(file_content.encode('utf-8'))

with open(file_name, 'rb') as f:
    files = {'file': (file_name, f)}
    response = session.post('https://httpbin.org/post', files=files)

print(f'Cookie: {cookie_value}')
print(f'File size: {file_size} в байтах')



