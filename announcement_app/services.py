import re
import time
import random

from bs4 import BeautifulSoup
from selenium import webdriver


def random_delay():
    delay_time = random.uniform(1, 3)
    time.sleep(delay_time)


def make_request(url):
    driver = webdriver.Firefox()
    driver.get('https://www.farpost.ru/' + url)
    html = driver.page_source
    driver.quit()
    return html


def get_page_urls_and_views(url):
    urls, views = [], []

    soup = BeautifulSoup(make_request(url), 'lxml')
    random_delay()
    _urls = soup.find_all('a', class_='bulletinLink bull-item__self-link auto-shy')
    random_delay()
    _views = soup.find_all('span', class_='views nano-eye-text')

    for index in range(10):
        url = _urls[index]['href']
        urls.append(url)

        view = _views[index].get_text(strip=True)
        view_count = re.search(r'\d+', view)
        views.append(view_count)

    return urls, views


def get_data_from_page(url):
    data = {}

    soup = BeautifulSoup(make_request(url), 'lxml')
    data['title'] = soup.find('span', attrs={'data-field': 'subject'}).get_text(strip=True)

    data['author'] = soup.find('span', class_='userNick auto-shy').get_text(strip=True)

    return data
