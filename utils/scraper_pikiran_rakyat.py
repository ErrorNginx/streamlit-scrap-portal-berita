from datetime import datetime
from bs4 import BeautifulSoup
import requests
from collections import Counter
import re
from .common.common import get_news_content, find_most_common_words, format_news_release_date

def scrape_pikiran_rakyat(url, headers):
    result = []
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        list_news = soup.find_all('div', class_='latest__item')
        for news in list_news[:10]:
            news_title = news.find(class_='latest__title').find(class_='latest__link').get_text(strip=True)
            news_release_date = news.find(class_='latest__date').get_text()
            news_link = news.find(class_='latest__title').find(class_='latest__link')['href']
            news_content = get_news_content(news_link, headers)
            most_common_words = find_most_common_words(news_content)
            scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result.append({
                "Tanngal scrapping": scrape_time,
                "Nama portal berita": "pikiran_rakyat",
                "Tanggal rilis berita": news_title,
                "Judul Berita": format_news_release_date(news_release_date),
                "URL Berita": news_link,
                "Kata sering muncul": ', '.join(most_common_words)  
            })
        pagination = soup.find('div', class_='paging')
        if pagination and pagination.find('a', class_='paging__link', string='Selanjutnya'):
            next_page_url = pagination.find('a', class_='paging__link', string='Selanjutnya')['href']
            next_page_url = f"https://www.pikiran-rakyat.com{next_page_url}"
            result += scrape_pikiran_rakyat(next_page_url, headers)
    return result
