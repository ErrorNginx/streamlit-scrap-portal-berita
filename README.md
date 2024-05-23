# 📰 Aplikasi Pencari Berita

Selamat datang di Aplikasi sracape Berita! Aplikasi ini memungkinkan Anda untuk mengumpulkan artikel berita dari berbagai portal berita Indonesia dan menampilkan kata-kata yang paling sering muncul digunakan dalam artikel tersebut. Aplikasi ini dibangun menggunakan Streamlit untuk UI dan BeautifulSoup untuk web scraping.

![Aplikasi Pencari Berita](https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Streamlit_logo.svg/1200px-Streamlit_logo.svg.png)

## Fitur

- **Mengambil Berita Terbaru**: Dapatkan artikel berita terbaru dari Pikiran Rakyat, Bandung Bisnis, dan Antaranews Jabar.
- **Presentasi Data**: Lihat data yang diambil dalam tabel interaktif.
- **Analisis Kata Umum**: Identifikasi dan tampilkan kata-kata yang paling sering muncul digunakan dalam artikel.
- **Unduh Data**: Unduh data yang diambil dalam format file JSON.

## Portal Berita

1. **Pikiran Rakyat**
   ![Pikiran Rakyat](https://upload.wikimedia.org/wikipedia/commons/6/6e/Logo_Pikiran_Rakyat.png)
2. **Bandung Bisnis**
   ![Bandung Bisnis](https://upload.wikimedia.org/wikipedia/commons/8/8e/Logo_Bisnis_Indonesia.svg)
3. **Antaranews Jabar**
   ![Antaranews Jabar](https://upload.wikimedia.org/wikipedia/commons/4/49/Antara_News_logo.png)

## Instalasi

Untuk menjalankan aplikasi ini secara lokal, ikuti langkah-langkah berikut:

1. **Clone repositori**:
    ```bash
    git clone https://github.com/usernameanda/news-scraper-app.git
    cd news-scraper-app
    ```

2. **Install paket yang dibutuhkan**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Jalankan aplikasi Streamlit**:
    ```bash
    streamlit run app.py
    ```

## Struktur Proyek
```bash
news-scraper-app/
│
├── app.py
├── requirements.txt
├── utils/
│ ├── common/
│ │ ├── init.py
│ │ ├── common.py
│ ├── init.py
│ ├── scraper_pikiran_rakyat.py
│ ├── scraper_bandung_bisnis.py
│ ├── scraper_antaranews_jabar.py
```


## Penggunaan

1. **Pilih Portal Berita**: Gunakan sidebar untuk memilih portal berita yang ingin Anda ambil.
2. **Ambil Berita**: Klik tombol untuk mulai mengambil artikel berita terbaru.
3. **Lihat Data**: Lihat data yang diambil dalam tabel interaktif.
4. **Unduh Data**: Unduh data yang diambil dalam format file JSON untuk analisis lebih lanjut.

## Kontribusi

Kontribusi sangat diterima! Silakan buka issue atau kirim pull request untuk fitur atau perbaikan bug.

## Penghargaan

- [Streamlit](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)

## Kontak

Untuk pertanyaan atau informasi lebih lanjut, silakan hubungi [agusmahari@gmail.com](agusmahari@gmail.com).

---