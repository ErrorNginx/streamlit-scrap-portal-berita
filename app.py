import streamlit as st
import pandas as pd
import json
from datetime import datetime
from utils.scraper_pikiran_rakyat import scrape_pikiran_rakyat
from utils.scraper_bandung_bisnis import scrape_bandung_bisnis
from utils.scraper_antaranews_jabar import scrape_antaranews_jabar


st.set_page_config(page_title="Aplikasi Scrap Portal Berita", page_icon=":berita:", layout="wide")

st.title("📰 Aplikasi Scrap Portal Berita")

# Sidebar menu
st.sidebar.header("Scraping Portal Berita")
menu = ["Pikiran Rakyat", "Bandung Bisnis", "Antaranews Jabar"]
choice = st.sidebar.selectbox("Pilih Portal Berita", menu)

# Headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

# URL for scraping
pikiran_rakyat_url = "https://www.pikiran-rakyat.com/jawa-barat"
bandung_bisnis_url = "https://bandung.bisnis.com/"
antaranews_jabar_url = "https://jabar.antaranews.com/"

if choice == "Pikiran Rakyat":
    st.subheader("🗞️ Pikiran Rakyat")
    if st.button('Scrape Portal Berita Pikiran Rakyat '):
        with st.spinner('Scraping Portal Berita Pikiran Rakyat...'):
            result = scrape_pikiran_rakyat(pikiran_rakyat_url, headers)
            st.success('Scraping Selesai!')
            df = pd.DataFrame(result)
            st.write("Berikut artikel berita terbaru dari Pikiran Rakyat:")
            st.dataframe(df)
            result_json = json.dumps(result, indent=4)
            st.download_button(
                label="Download data as JSON",
                data=result_json,
                file_name=f"scraped_pikiran_rakyat_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json",
                mime='application/json'
            )

elif choice == "Bandung Bisnis":
    st.subheader("💼 Bandung Bisnis ")
    if st.button('Scrape Portal Berita Bandung Bisnis'):
        with st.spinner('Scraping Portal Berita Bandung Bisnis...'):
            result = scrape_bandung_bisnis(bandung_bisnis_url, headers)
            st.success('Scraping Selesai!')
            df = pd.DataFrame(result)
            st.write("Berikut artikel berita terbaru dari Bandung Bisnis:")
            st.dataframe(df)
            result_json = json.dumps(result, indent=4)
            st.download_button(
                label="Download data as JSON",
                data=result_json,
                file_name=f"scraped_bandung_bisnis_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json",
                mime='application/json'
            )

elif choice == "Antaranews Jabar":
    st.subheader("📢 Antaranews Jabar News")
    if st.button('Scrape Portal Berita Antaranews Jabar'):
        with st.spinner('Scraping Portal Berita Antaranews Jabar...'):
            result = scrape_antaranews_jabar(antaranews_jabar_url)
            st.success('Scraping Selesai!')
            df = pd.DataFrame(result)
            st.write("Berikut artikel berita terbaru dari Antaranews Jabar:")
            st.dataframe(df)
            result_json = json.dumps(result, indent=4)
            st.download_button(
                label="Download data as JSON",
                data=result_json,
                file_name=f"scraped_antaranews_jabar_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json",
                mime='application/json'
            )
