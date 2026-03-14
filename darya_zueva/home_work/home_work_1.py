import requests

def get_json():
    with requests.Session() as session:
        response = session.get('https://httpbin.org/json')
        response.raise_for_status()
        title = response.json()
        print(f"Title: {title['slideshow']['title']}")
        return get_post(session)

def get_post(session):
    url = 'https://httpbin.org/post'
    data = {'username': 'test_user','password': 'qwerty'}
    try:
        response = session.post(url, data=data)
        response.raise_for_status()
        result_form = response.json()['form']
        print(result_form)
    except requests.exceptions.HTTPError:
        print(f"Ошибка: {response.status_code}")
    except requests.exceptions.RequestException:
        print("Сервер недоступен")

get_json()