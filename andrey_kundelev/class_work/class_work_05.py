import allure
import requests
from allure_commons.types import Severity, LabelType  # LabelType, не LabelTypes

@allure.title('Тест для проверки сайта')
@allure.description('Тест проверяет сайт пупкин на доступность статус-кода')
@allure.tag('smoke', 'web', 'positive')
@allure.severity(Severity.NORMAL)
@allure.label(LabelType.FRAMEWORK, 'pytest')
@allure.label(LabelType.LANGUAGE, 'python')
@allure.id('')


def test_pupkin_status_code():
    with allure.step('Подготовка тестовых данных'):
        with allure.step('Вызов метода docs/v2/install-for-windows'):
            response = requests.get('https://allurereport.org/docs/v2/install-for-windows/')  # requests, не request

    with allure.step('проверка ответа'):
        assert response.status_code == 200
