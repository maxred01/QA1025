import requests
import pytest


@pytest.mark.parametrize('param', [
    ('151516'),
    ('gahsrjt'),
    ('#$$@$%^$#'),
])
def test_param(param):
    URL = "https://store.steampowered.com/"

    requests = requests.request(method='GET',
                                url=URL,
                                params={'War_Thunder': param}
    )

print(requests.status_codes)

assert requests.status_codes == 200, f'Статус код не равен 200. Статус код равен {requests.status_codes}'

