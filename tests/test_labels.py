import allure
from allure_commons.types import Severity

#разметка тестов

def test_dinamic_labels(): #подход - тест как сценарий
    allure.tag('web')
    allure.severity(Severity.BLOCKER)
    allure.label('Задачи и репозитории')
    allure.story('Неавторизованный пользователь не может создавать задачу в репозитории')
    allure.link('https//:github.com', name='Testing')
    pass

#предпочтительный подход разметки
@allure.tag('web')
@allure.severity(Severity.CRITICAL) #редко
@allure.label('owner', 'eroshenkoam') #часто
@allure.feature('Задачи и репозитории') #постоянно
@allure.story('Авторизованный пользователь может создавать задачу в репозитории') #постоянно
@allure.link('https//:github.com', name='Testing') #часто, но динамические


def test_decorator_labels(): #степы через декораторы
    pass
