import requests
import pytest

URL = 'https://httpbin.org/basic-auth/'
data = '200'

@pytest.fixture()
def get_status():
    url = 'https://httpbin.org/ip'
    response = requests.get(url=url)
    return response


def test_check_ip(get_status):
    assert get_status.status_code == 200
    assert get_status.json()['origin'] == "212.98.190.37"


@pytest.fixture()
def auth_get_status():

    user = 'user'
    passwd = 'passwd'
    url = f'https://httpbin.org/basic-auth/{user}/{passwd}'
    response = requests.get(url=url, auth=("user", "passwd"))

    return response


def test_status_code(auth_get_status):
    assert auth_get_status.status_code == 200


def test_check_body_auth(auth_get_status):

    data = auth_get_status
    assert data.json()['authenticated'] is True
    assert data.json()['user'] == 'user'
