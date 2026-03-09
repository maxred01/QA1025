import requests as Req
import pytest


@pytest.mark.parametrize('param', [
    ('12342'),
    ('выпавыавфыа'),
    ('fdsfdsfdsafas'),
    (' "№;%:? *(" '),
])
def test_param(param):
    URL = 'https://hoster.by/service/domains/'

    requests = Req.request(method='GET',
                           url=URL,
                           params={'domain_name': param})

    print(requests.text)

    assert requests.status_code == 201, f'Статус код не равен 201. Статус код равен {requests.status_code}'
