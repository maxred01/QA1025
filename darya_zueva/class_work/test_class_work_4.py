import requests as Req
import pytest


@pytest.mark.parametrize('param', [
    ('13213123'),
    ('qrwrwwq'),
    ('укпукпукп'),
    ('укпукпукп'),
])
def test_param(param):
    URL = 'https://www.networksolutions.com/products/domain/'

    requests = Req.request(method='GET',
                        url=URL,
                        params={'domain-search-results': param})

    print(requests.text)

    assert requests.status_code == 201, f'Статус код не равен 201. Статус код равен {requests.status_code}'

