import allure
import requests
from allure_commons.types import Severity

URL = 'https://allurereport.org/docs/pytest/'


@allure.title("Тест для проверки сайта allurereport.org/docs")
@allure.description("Сайт проверяется с помощью assert.status_code")
@allure.tag("smok_test, web-site, positive")
@allure.label(label_type="framework")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("тест для проверки статус кода")
def test_status_code():
    with allure.step("Подготовка тестовых данных"):
        with allure.step("Вызов метода get"):
            response = requests.get(url=URL)
    with allure.step("Проверка статус кода"):
        assert response.status_code == 200


def test_allure_modul():
    url = 'https://allurereport.org/modules/'
    response = requests.get(url=url)
    print(response.headers)
