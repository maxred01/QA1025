import requests


def test_status_code():
    URL = 'https://httpbin.org/ip'
    status_code = 200
    origin = '212.98.190.37'

    response = requests.get(url=URL)
    new_responce = response.json()

    assert response.status_code == status_code, \
        f'Неверный статус кода. Ожидался {status_code}, получен {response.status_code}'
    assert new_responce['origin'] == origin, f'Неверный ответ от origin. Получен {new_response['origin']}, Ожидается {origin}'