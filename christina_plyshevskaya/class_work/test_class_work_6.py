import allure
import requests
from allure_commons.types import Severity, LabelType
@allure.title('тест на проверку сайта')
@allure.description('тест проверяет сайт ларисы долиной на доступность при помощи ответа статус кода')
@allure.tag('smoke', 'web', 'positive')
@allure.severity(Severity.NORMAL)
@allure.label(LabelType.FRAMEWORK, 'pytest')
@allure.label(LabelType.LANGUAGE, 'python')
@allure.id('123')


def test_larisa_dolina_status_code():
    with allure.step('подготовка тестовых данных'):
        with allure.step('вызов метода /news/'):
            response = requests.get('https://larisadolina.com/news/')

    with allure.step('проверка ответа'):
        assert response.status_code == 200

        with allure.step('проверка ответа'):
            assert response.status_code == 200

            with allure.step('проверка ответа'):
                assert response.status_code == 200

    with allure.step('проверка ответа'):
        assert response.status_code == 200