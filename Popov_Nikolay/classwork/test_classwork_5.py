import allure
import requests
from allure_commons.types import Severity, LabelType
import json

URL = 'https://artmas.by'


catalog = 'catalog'
response = requests.get(url=f'{URL}')
print(response.status_code)


# @allure.title("Тест для проверки сайта https://artmas.by")
# @allure.description("Тест сайта для сайта проверяет его доступность")
# @allure.tag("smok_test, web-site, positive")
# @allure.label(LabelType.FRAMEWORK, 'pytest')
# @allure.label(LabelType.LANGUAGE, 'python')
# @allure.severity(allure.severity_level.NORMAL)
# @allure.feature("тест для проверки статус кода")
# def test_status_code():
#     with allure.step("Вызов метода request.get"):
#             response = requests.get(url=URL)
#
#     with allure.step("Проверка статус кода"):
#         assert response.status_code == 200
#
#
# def test_catalog():
#     catalog = 'catalog'
#     with allure.step("Вызов метода get()"):
#         response = requests.get(url=f'{URL}/{catalog}')
#
#     with allure.step("Проверка json файла"):
#         data = response.json()
#         print(f"Response Content (first 200 chars): {response.text[:200]}")