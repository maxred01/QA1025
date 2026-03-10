import requests as Req
import pytest


@pytest.mark.parametrize('param', [
    ('12321'),
    ('sdfsdf'),
    ('ваыаa'),
    ('#$%^&*( ')
])
def test_param(param):
    URL = 'https://itstep.by/'

    requests = Req.request(method='GET',
                           url=URL,
                           params={'domain_name': param}
                           )

    print(requests.request)

    assert requests.status_code == 201, f'Статус-код не равен 201. Статус код равен {requests.status_code}'
