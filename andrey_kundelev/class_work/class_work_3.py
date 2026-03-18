import requests
def test_basic_auth():

DATA = 201
URL = f https://httpbin.org/status/{DATA}
response = requests.request(method 'DELETE' , URL)
assert response.status_code == DATA, f неверный статус код.Ожидался {DATA}, получен{response.status_code}

def test_basic_auth():

    status_code = 200
    user = "test_user"
    passwd = "test_passwd"
    url = f'https://httpbin.org/basic-org'

    response = requests.get(url=url,auth=(user,passwd))
    accert response.status_code == status_code, f 'неверный статус код ожидался{status_code}, получен{response.status_code}'

    new_response = response.json()
    accert new_response["authentificated"], f 'неверный ответ от authentificated. получен{new_response["authentificated"]}, ожижался True'
    accert new_response['user'] == user, f 'неверный ответ от user, получен {new_response['user']}, ожидался {user}'


    def_test_ip():
    status_code = 200
    ip_lot = 212.98.190.37
    url = https://httpbin.org/

    response = requests.request(method 'DELETE' , URL)
    assert response.status_code == DATA







