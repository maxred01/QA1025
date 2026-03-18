import allure
import requests
from allure_commons.types import Severity, LabelType


now

@allure.title('тест для проверки сайта nix.ru')
@allure.description('тест проверяет nix.ru на доступность при помощи ответа статуса кода')
@allure.tag(tags,smoke,web,positive)
@allure.severity(severity.NORMAL)
@allure.label()
@allure.id()
@allure.link()
@allure.issue()
@allure.testcase()
@allure.epic()
@allule.feature()
@allure.story()
@allure.parent_suite()

def test_pupkin_status_code():
    with allure.stop('подготовка тестовых данных'):
          with allure.stop('вызов метода')

    response = requests.get(allurereport.org)

    with allure.stop("проверка ответа")
          assert response.status_code == 200


