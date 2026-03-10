# Задание
# Отправьте GET-запрос на https://httpbin.org/json.
# Извлеките значение поля slideshow.title из ответа.
# Выведите результат в формате:
# Title: [НАЙДЕННЫЙ_ЗАГОЛОВОК]


import requests as Req
import pytest


# @pytest.mark.parametrize('param', [
#     ('12321'),
#     ('sdfsdf'),
#     ('ваыа'),
#     ('#$%^&*( ')
# ])
def test_param(param):
    URL = 'https://httpbin.org/json'

    requests = Req.request(method='GET',
                           url=URL,
                           params={'domain_name': param}
#                          )
    print(requests.request)
#
#     assert requests.status_code == 201, f'Статус-код не равен 201. Статус код равен {requests.status_code}'
