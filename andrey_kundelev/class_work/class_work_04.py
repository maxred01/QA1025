import requests

def test_status_code():
    DATA = 201
    URL = f'https://httpbin.org/status{DATA}'
    response = requests.request('DELETE', URL)
    assert response.status_code == DATA, f'Статус-код не равен {DATA}. Статус код равен {response.status_code}'



def test_basic_auth():

    status_code = 200 #подготовка тестовых данных
    user = 'test_user'
    passwd = 'test_passwd'
    url = f'https://httpbin.org//basic-auth/{user}/{passwd}'

    response = requests.get(url=url, auth=('user', 'passwd')) #Действия

        f'Статус-код не равен 201. Ожидался {status_code} Статус код равен {response.status_code}'

    new_response = response.json
    assert new_response['authenticated'], f'Неверный ответ от autheticated. Получен {new_response['authenticated']}, ожидался True' #Проверка
    assert new_response['user'] == user, f'Неверный ответ от user. Получен {new_response['user']}, ожидался {user}'


def test_nix_get():
    url = 'https://www.nix.ru/'
    payload = {}

    headers{

  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
  -b 'BasketCopyOfSSID=c343d7994186c710deab8821594e4228; CityKLADR=0c5b2444-70a0-4932-980c-b4dc0d3f02b5; PHPSESSID=c2927f6c7b8a325321d69291f2183564' \
  -H 'priority: u=0, i' \
  -H 'sec-ch-ua: "Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url)
    print(response.text)
    assert response.status_code == 200

def test_ip_get():
    status_code = 200  # подготовка тестовых данных
    url = 'https://httpbin.org/ip'

    response = requests.request("GET", url)

    assert response.status_code == 200, f'Ожидался {status_code} Статус код равен {response.status_code}'
    assert response['origin'] == 212.98.190.37, f'Неверный ответ от user. Получен {response['origin']}, ожидался {212.98.190.37}'
    #скорость, атомарность, распределенный запуск(многопоточность, поддержка распределенного запуска),
    # тесты не должны изменять тестовую среду, понятное название,
    # поддержка теста(не нужно писать замудремные тесты, которые сложно поддерживать)

