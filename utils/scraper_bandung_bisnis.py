from datetime import datetime
from bs4 import BeautifulSoup
import requests
from collections import Counter
import re
from .common.common import get_top_words_and_date

def scrape_bandung_bisnis(url, headers):
    result = []
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        news_container = soup.find_all("div", class_="artItem")[:10]
        scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for news in news_container:
            title = news.find("h4", class_="artTitle").get_text(strip=True)
            link = news.find("a", class_="artLink")["href"]
            full_url = link if link.startswith("http") else "https://bandung.bisnis.com" + link
            top_words, release_date = get_top_words_and_date(full_url, headers)
            news_item = {
                "Tanngal scrapping": scrape_time,
                "Nama portal berita": "bandung_bisnis_com",
                "Tanggal rilis berita": release_date,
                "Judul Berita": title,
                "URL Berita": full_url,
                "Kata sering muncul": ', '.join(top_words)  
            }
            result.append(news_item)
    return result
