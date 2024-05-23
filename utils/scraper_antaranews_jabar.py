from datetime import datetime
from bs4 import BeautifulSoup
import requests
from .common.common import find_most_common_words

def scrape_antaranews_jabar(url):
    result = []
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    terkini_section = soup.find('div', class_='terkininew col-md-12')
    articles = terkini_section.find_all('article', limit=10) if terkini_section else []

    for article in articles:
        title_tag = article.find('h3')
        title = title_tag.get_text(strip=True) if title_tag else "No Title"
        link_tag = article.find('a', href=True)
        link = link_tag['href'] if link_tag else "No Link"
        scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if link != "No Link":
            article_response = requests.get(link)
            article_response.raise_for_status()
            article_soup = BeautifulSoup(article_response.text, 'html.parser')
            content_div = article_soup.find('div', class_='post-content') or article_soup.find('div', class_='entry-content')
            content = content_div.get_text(strip=True) if content_div else "No Content"
            date_tag = article_soup.find('span', class_='article-date')
            release_date = date_tag.get_text(strip=True) if date_tag else "No Date"
            most_common_words = find_most_common_words(content) if content != "No Content" else []
        else:
            content = "No Content"
            most_common_words = []
            release_date = "No Date"

        result.append({
            'Tanngal scrapping': scrape_time,
            'Nama portal berita': 'antaranews_jabar',
            'Tanggal rilis berita': release_date,
            'Judul Berita': title,
            'URL Berita': link,
            'Kata sering muncul': ', '.join(most_common_words)  # Convert list to string
        })
    return result
