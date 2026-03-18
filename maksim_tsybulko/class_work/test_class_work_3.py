import requests


def test_status_code():
    daa = 201
    url = f'https://httpbin.org/status/{daa}'

    response = requests.request('DELETE', url)

    assert response.status_code == daa, f'Неверный статус код. Ожидался {daa}, получен {response.status_code}'


def test_basic_auth():

    status_code = 200
    user = 'test_user'
    passwd = 'test_passwd'
    url = f'https://httpbin.org/basic-auth/{user}/{passwd}'

    response = requests.get(url=url, auth=(user, passwd))
    new_response = response.json()

    assert response.status_code == status_code, \
        f'Неверный статус код. Ожидался {status_code}, получен {response.status_code}'
    assert new_response['authenticated'], f'Неверный ответ от authenticated. Получен {new_response['authenticated']}, ожидался True'
    assert new_response['user'] == user, f'Неверный ответ от user. Получен {new_response['user']}, ожидался {user}'


def test_nix_get():
    url = "https://www.nix.ru/"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'if-modified-since': 'Mon, 16 Mar 2026 18:20:00 GMT',
        'if-none-match': '"859cec0d2ae6026c43e20a125ce2270c-gzip"',
        'priority': 'u=0, i',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.history)
