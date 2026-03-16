import requests

def test_basic_auth():
    status_code = 200
    user = 'user_test'
    passwd = 'password_test'
    URL = f'https://httpbin.org/basic-auth/{user}/{passwd}'

    response = requests.get(url=URL, auth=(user, passwd))
    new_response = response.json()

    assert response.status_code == status_code, \
        f'Неверный статус кода. Ожидался {status_code}, получен {response.status_code}'
    assert new_response['authenticated'], f'Неверный ответ от authenticated. Получен {new_response['authenticated']}, Ожидается True'
    assert new_response['user'] == user, f'Неверный ответ от authentication. Получен {new_response['user']}, ожидался {user}'