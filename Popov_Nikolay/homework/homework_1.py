import requests


# 1. Отправьте GET-запрос на https://httpbin.org/json.
# 2. Извлеките значение поля slideshow.title из ответа.
# 3. Выведите результат в формате:
# Title: [НАЙДЕННЫЙ_ЗАГОЛОВОК]
#


def get_json():
    with requests.session() as session:
        URL = 'https://httpbin.org/json'
        response = session.get(url=URL)
        title = response.json()
        print(f"Title: {title['slideshow']['title']}")
        return get_post(session)


def get_post(session):
    URL = 'https://httpbin.org/post'
    data = {
        'username': 'test_user',
        'password': 'qwerty'
    }
    headers = {
        "Accept": "application/json"
    }
    try:
        response = session.post(url=URL,
                                json=data,
                                headers=headers)

        response.raise_for_status()
        return response.json()['form']


    except requests.exceptions.HTTPError as http_err:
        return f'Ошибка http - соединения: {http_err}'
    except requests.exceptions.RequestException as req_except:
        return f'Ошибка запроса - {req_except}'



def get_test_cookies(session):
    url_1 = 'https://httpbin.org/cookies/set/test_cookie/12345'
    session.get(url=url_1)

    url_2 = 'https://httpbin.org/cookies'
    response = session.get(url=url_2)
    return response.json()


def post_cookies(session):
    url = 'https://httpbin.org/post'
    try:
        response = session.post(
            url=url,
            json=get_test_cookies(session)
        )
        response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        return f'Ошибка http - соединения: {http_err}'
    except requests.exceptions.RequestException as req_except:
        return f'Ошибка запроса - {req_except}'

def get_cookies(session):
    url = 'https://httpbin.org/cookies'
    response = session.get(url=url)
    cookies_data = response.json()
    print(f'Cookies: {cookies_data['cookies']}',  f'Size: {int(response.headers['content-length'])} байт', sep='\n')


if __name__ == '__main__':
    with requests.Session() as session:
        print(get_json())
        post_cookies(session)
        get_cookies(session)
