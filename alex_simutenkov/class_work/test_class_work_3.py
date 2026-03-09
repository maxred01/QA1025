import requests as re
import pytest


@pytest.mark.paramrize('param', [
    ('1546768'),
    ("GFHGHGHGJ"),
    (878768768),
    (1007547954)])
def test_param(param):
    URL = "https://www.nix.ru"

    requests = re.request(method='GET',
                          url=URL,
                          params={'drfghj': param}
                          )

    print(requests.request)

    assert requests.status_code == 201, f'Статус код не равен 201. Статус код равен {requests.status_code}'
