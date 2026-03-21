import pytest
import requests
from bs4 import BeautifulSoup

URL = 'https://artmas.by'
catalog = 'catalog'
projects = 'projects'
designers = 'designers'
blog = 'blog'


@pytest.fixture()
def main_page():

    response = requests.get(url=URL)
    return response


@pytest.mark.parametrize('page',
                         ["",
                         "catalog",
                         "projects",
                         "designers",
                         "blog"]
                         )
def test_all_pages_status_code_200(page):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    url = f'{URL}/{page}'.strip('/')
    response = session.get(url)
    assert response.status_code == 200, f'Страница {page} не активна. Статус кода: {response.status_code}'


def check_headers_content_type(response):
    assert response == 'text/html; charset=UTF-8'


def check_title_page(response, name_page):
    assert response == name_page


@pytest.mark.parametrize('page',
                         ["",
                         "catalog",
                         "projects",
                         "designers",
                         "blog"]
                         )
def test_headers_text_html_all_pages(page):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    response = session.get(url=f'{URL}/{page}')
    content_type = response.headers["content-type"]

    check_headers_content_type(content_type)

@pytest.mark.parametrize('page, page_title',
                         [
                         ("", "Дизайнерская мягкая мебель ARTMAS - Минск, Москва, Санкт-Петербург"),
                         ("catalog", "Каталог товаров"),
                         ("projects", "Проекты"),
                         ("designers", "Дизайнерам"),
                         ("blog", "Блог"),
                         ])
def test_all_pages_title(page, page_title):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    if page == "":
        url = f'{URL}'
        response = session.get(url=url)
        soup = BeautifulSoup(response.text, 'html.parser').title.string
        assert 'Дизайнерская мягкая мебель ARTMAS' in soup
    else:
        url = f'{URL}/{page}'.strip('/')
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser').title.string
        check_title_page(soup, page_title)
