from bs4 import BeautifulSoup
from collections import Counter
import re
import requests

# List of stopwords
stopwords = [
    'dan', 'dari', 'di', 'dengan', 'ke', 'oleh', 'pada', 'sejak', 'sampai', 'seperti', 
    'untuk', 'buat', 'bagi', 'akan', 'antara', 'demi', 'hingga', 'kecuali', 'tentang', 
    'serta', 'tanpa', 'kepada', 'daripada', 'oleh karena itu', 'antara', 'dengan', 'sejak', 
    'sampai', 'bersama', 'beserta', 'menuju', 'menurut', 'sekitar', 'selama', 'seluruh', 
    'bagaikan', 'terhadap', 'melalui', 'mengenai', 'yang', 'ini', 'tersebut'
]

def get_news_content(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        news_content = soup.find('article', class_='read__content')
        
        if news_content:
            paragraphs = news_content.find_all('p')
            text = ' '.join([p.get_text(strip=True) for p in paragraphs])
            return text
        else:
            return ""
    else:
        return ""

def find_most_common_words(text, limit=5):
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in stopwords]
    word_freq = Counter(filtered_words)
    most_common_words = [word for word, _ in word_freq.most_common(limit)]
    return most_common_words

def format_news_release_date(release_date):
    try:
        date_part, time_part = release_date.split(', ')
        time_part = time_part.replace(' WIB', '')
        if len(time_part.split(':')) == 2:
            time_part += ':00'
        day, month_name, year = date_part.split()
        indonesia_month_map = {
            'Januari': '01',
            'Februari': '02',
            'Maret': '03',
            'April': '04',
            'Mei': '05',
            'Juni': '06',
            'Juli': '07',
            'Agustus': '08',
            'September': '09',
            'Oktober': '10',
            'November': '11',
            'Desember': '12'
        }
        month = indonesia_month_map[month_name]
        formatted_date_string = f"{year}-{month}-{day} {time_part}"
        return formatted_date_string
    except Exception:
        return release_date

def get_top_words_and_date(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        article_content = soup.find("article", class_="detailsContent")
        release_date = soup.find("div", class_="detailsAttributeDates").get_text(strip=True)
        if article_content:
            paragraphs = article_content.find_all("p")
            text = " ".join([p.get_text() for p in paragraphs])
            words = re.findall(r'\b\w+\b', text.lower())
            filtered_words = [word for word in words if word not in stopwords]
            common_words = Counter(filtered_words).most_common(5)
            return [word for word, _ in common_words], release_date
    except requests.exceptions.RequestException as e:
        return [], ""
