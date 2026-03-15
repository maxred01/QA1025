import requests

# response = requests.get('https://httpbin.org/json')
# print(response.status_code)
# data = response.json()
# title = data["slideshow"]["title"]
# print(f'Title: {title}')
#
# params = {'page': 2, 'limit': 10}
# response = requests.get('https://httpbin.org/get', params=params)
# print(response.url)  # URL с параметрами: https://httpbin.org/get?page=2&limit=10


from requests.exceptions import HTTPError, RequestException
data = {'username': 'test_user', 'password': 'qwerty'}
url = 'https://httpbin.org/post'
try:
    response = requests.post(url, data=data)
    response.raise_for_status()
    form_data = response.json()['form']
    print(f"Содержимое ключа: {form_data}")
except HTTPError as e:
        print(f"Ошибка: {response.status_code}")
except RequestException as e:
      print("Сервер недоступен")
