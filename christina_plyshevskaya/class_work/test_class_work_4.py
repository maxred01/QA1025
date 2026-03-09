import requests as Req
import pytest

@pytest.mark.parametrize('param', [
    ('245354'),
    ('jsfdsfds'),
    ('влвлвлвлвл'),
])
def test_param(param):
    URL = 'https://larisadolina.com/events/'

    requests = Req.request(method='GET',
                            url=URL,
                            params={'events': param})

    print(requests.encoding)
    assert requests.status_code == 201, f'Статус код не равен 201. Статус код равен {requests.status_code}'
