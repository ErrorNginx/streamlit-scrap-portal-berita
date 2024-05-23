# 📰 Aplikasi Pencari Berita

Selamat datang di Aplikasi sracape Berita! Aplikasi ini memungkinkan Anda untuk mengumpulkan artikel berita dari berbagai portal berita Indonesia dan menampilkan kata-kata yang paling sering muncul digunakan dalam artikel tersebut. Aplikasi ini dibangun menggunakan Streamlit untuk UI dan BeautifulSoup untuk web scraping.


## Fitur

- **Mengambil Berita Terbaru**: Dapatkan artikel berita terbaru dari Pikiran Rakyat, Bandung Bisnis, dan Antaranews Jabar.
- **Presentasi Data**: Lihat data yang diambil dalam tabel interaktif.
- **Analisis Kata Umum**: Identifikasi dan tampilkan kata-kata yang paling sering muncul digunakan dalam artikel.
- **Unduh Data**: Unduh data yang diambil dalam format file JSON.

## Portal Berita

1. **Pikiran Rakyat**
2. **Bandung Bisnis**
3. **Antaranews Jabar**

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
├── README.md
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