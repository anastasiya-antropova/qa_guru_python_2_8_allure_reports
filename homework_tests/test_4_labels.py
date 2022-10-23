import allure
from allure_commons.types import Severity
import test_2_3_steps as steps

def test_dynamic_labels():
    allure.dynamic.tag('web', 'homework')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label('owner', 'antropovaaa')
    allure.dynamic.feature('Задачи и репозитории')
    allure.dynamic.story('Неавторизованный пользователь не может создавать задачу в репозитории')
    allure.dynamic.link('https//:github.com', name='Testing')

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'antropovaaa')
@allure.feature('Задачи и репозитории')
@allure.story('Авторизованный пользователь может создавать задачу в репозитории')
@allure.link('https//:github.com', name='Testing')

def test_decorator_labels():
    steps.open_main_page()
    steps.search_for_repository('anastasiya-antropova/qa_guru_python_2_6_files')
    steps.go_to_repository('anastasiya-antropova/qa_guru_python_2_6_files')
    steps.open_issue_tab()
    steps.should_see_issue_with_number('New issue')