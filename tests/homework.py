import allure
from allure_commons.types import Severity
from selene import browser, by, have, be
from selene.support.shared.jquery_style import s

#from pages.search_issue import Issue

repository = 'eroshenkoam/allure-playwright-example'
actual_text = 'Не работает переход по табу Issues'
path_directory = 'Meshchenenkov/QAGURUhw5'

# 1. Чистый Selene (без шагов)
@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner')
@allure.feature('Задачи в репозитории')
@allure.story(f'Неавторизованный пользователь проверяет наличие задачи в репозитории')
@allure.link('https://github.com')
def test_github(setup_browser):
    browser.open('https://github.com')

    s(".search-input").click()
    s("#query-builder-test").send_keys(path_directory).press_enter()
    s(by.link_text(path_directory)).click()
    s("#issues-tab").click()
    s(by.css("[data-testid='issue-pr-title-link']")).should(have.exact_text('test_issue'))


# 2. Лямбда шаги через with allure.step
@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner')
@allure.feature('Задачи в репозитории')
@allure.story(f'Неавторизованный пользователь проверяет наличие задачи в репозитории')
@allure.link('https://github.com')
def test_allure_steps(setup_browser):
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозитория"):
        s(".search-input").click()
        s("#query-builder-test").send_keys(path_directory).press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text(path_directory)).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с текстом 'test_issue'"):
        s(by.css("[data-testid='issue-pr-title-link']")).should(have.exact_text('test_issue'))


# 3. Шаги с декоратором @allure
@allure.tag('Web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner')
@allure.feature('Задачи в репозитории')
@allure.story(f'Неавторизованный пользователь проверяет наличие задачи в репозитории')
@allure.link('https://github.com')
def test_decorator_steps(setup_browser):
    open_main_page()
    search_for_repository(path_directory)
    go_to_repository(path_directory)
    open_issue_tab()
    should_see_issue_with_title("test_issue")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".search-input").click()
    s("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с текстом {text}")
def should_see_issue_with_title(text):
    s(by.css("[data-testid='issue-pr-title-link']")).should(have.exact_text(text))