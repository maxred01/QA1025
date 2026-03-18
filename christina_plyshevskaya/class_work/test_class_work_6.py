import allure
import requests
from allure_commons.types import Severity, LabelType
@allure.title('тест на проверку сайта')
@allure.description('тест проверяет сайт пупкин на доступность при помощи ответа статус кода')
@allure.tag('smoke', 'web', 'positive')
@allure.severity(Severity.NORMAL)
@allure.label(LabelType.FRAMEWORK, 'pytest')
@allure.label(LabelType.LANGUAGE, 'python')
@allure.id('123')


def test_pupkin_status_code():
    with allure.step('подготовка тестовых данных'):
        with allure.step('вызов метода docs/v2/install-for-windows'):
            response = requests.get('https://allurereport.org/docs/v2/install-for-windows/')

    with allure.step ('проверка ответа'):
        assert response.status_code == 200

        with allure.step('проверка ответа'):
            assert response.status_code == 200

            with allure.step('проверка ответа'):
                assert response.status_code == 200

    with allure.step('проверка ответа'):
        assert response.status_code == 200