import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dinamic_steps():
    with allure.step('Open main page'):
        browser.open('https://github.com')

    with allure.step('Find repository'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step('Transition'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Open Issue'):
        s('#issues-tab').click()

    with allure.step('Check Issue with #76'):
        s(by.partial_text("#76")).should(be.visible)

def test_decorator_steps(): #степы через декораторы
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('76')

@allure.step('Open main page') #итератор
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

@allure.step('Should see issue with number {number}')
def should_see_issue_with_number(number):
    s(by.partial_text('#' + number)).should(be.visible)