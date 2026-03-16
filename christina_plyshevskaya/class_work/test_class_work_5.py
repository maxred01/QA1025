import requests
def test_status_code():
    daa = 201
    URL = f'https://httpbin.org/status/{daa}'
    response = requests.request('DELETE', URL)
    assert response.status_code == daa, f'Неверный статус код. Ожидается {daa}, получен {response.status_code}'

def test_basic_auth():

    status_code = 200
    user = 'test_user'
    passwd = 'test_passwd'
    url = f'https://httpbin.org/basic-auth/{user}/{passwd}'

    response = requests.request(url=url, auth=(user, passwd))
    new_response = response.json()

    assert response.status_code == status_code, f'Неверный статус код. Ожидается {status_code}, получен {response.status_code}'
    assert new_response["authenticated"], f'Неверный ответ от authenticated. Получен{new_response["authenticated"]}, ожидается True'
    assert new_response["user"] == user, f'Неверный ответ от user. Получен{new_response["user"]}, ожидается {user}'

def test_ip():

    status_code = 200
    origin = '212.98.190.37'
    url = f'https://httpbin.org/ip'

    response = requests.request('GET', url=url)

    assert response.status_code == status_code, f'Неверный статус код. Ожидается {status_code}, получен {response.status_code}'

