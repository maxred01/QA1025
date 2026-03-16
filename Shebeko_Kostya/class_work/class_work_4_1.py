import requests

DATA = 201
URL = f'https://httpbin.org/status/{DATA}'

response = requests.request(method='DELETE', URL)

assert response.status_code == DATA, f'Неверный статус код.Ожидался {DATA}, получен {response.status_code}'


