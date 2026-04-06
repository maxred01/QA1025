import allure
import requests
from allure_commons.types import Severity, LabelType

@allure.title('Тест для проверки сайта')
@allure.description('Тест проверяет itspep на доступность при помощи ответа статус кода')
@allure.tag('smoke', 'web', 'positive')
@allure.severity(Severity.NORMAL)
@allure.label(LabelType.FRAMEWORK, 'pytest')
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.epic("Web interface")
@allure.feature("Essential features")
@allure.story("Authentication")
@allure.parent_suite("Tests for web interface")
@allure.suite("Tests for essential features")
@allure.sub_suite("Tests for authentication")
def test_pupkin_status_code():
    with allure.step('Подготовка тестовых данных'):
        headers = {

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        }
        with allure.step('Вызов метода docs/v2/install-for-windows'):
            response = requests.get('https://itstep.by/', headers=headers)

    with allure.step('Проверка ответа'):
        assert response.status_code == 200

        with allure.step('Проверка ответа'):
            assert response.status_code == 200

            with allure.step('Проверка ответа'):
                assert response.status_code == 200

    with allure.step('Проверка ответа'):
        assert response.status_code == 200