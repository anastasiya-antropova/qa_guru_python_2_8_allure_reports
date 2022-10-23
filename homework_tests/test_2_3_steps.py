import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step('Open main page'):
        browser.open('https://github.com')

    with allure.step('Find repository'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('anastasiya-antropova/qa_guru_python_2_6_files')
        s('.header-search-input').submit()

    with allure.step('Transition'):
        s(by.link_text('anastasiya-antropova/qa_guru_python_2_6_files')).click()

    with allure.step('Open Issue'):
        s('#issues-tab').click()

    with allure.step('Check Issue with New issue'):
        s(by.partial_text('New issue')).should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_for_repository('anastasiya-antropova/qa_guru_python_2_6_files')
    go_to_repository('anastasiya-antropova/qa_guru_python_2_6_files')
    open_issue_tab()
    should_see_issue_with_number('New issue')

@allure.step('Open main page')
def open_main_page():
    browser.open('https://github.com')

@allure.step('Search for repository {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()

@allure.step('Go to repocitory {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step('Open Issue tab')
def open_issue_tab():
    s('#issues-tab').click()

@allure.step('Should see issue with number {new_issue}')
def should_see_issue_with_number(new_issue):
    s(by.partial_text(new_issue)).should(be.visible)