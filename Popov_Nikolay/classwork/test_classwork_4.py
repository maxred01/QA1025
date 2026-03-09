import requests
import pytest


@pytest.mark.parametrize("param", [
    ("categories"),
    ("nalichie-na-sklade"),
    ("super-ceny"),
    ("nepohozhest-kak-pravilo"),
    ("credit")
])
def test_param(param):
    URL = 'https://www.divan.by/'
    param = {}

    response = requests.request(method='get', url=URL, params=param)

    status = response.status_code

    assert status == 200, f"Статус код равен - {status}"
