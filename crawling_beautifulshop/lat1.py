import requests
from bs4 import BeautifulSoup

# Mengirim permintaan HTTP ke halaman web
url = 'https://www.example.com'
response = requests.get(url)

# Menganalisis konten halaman web menggunakan BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Menemukan elemen yang ingin diekstrak
titles = soup.find_all('h3', class_='title')

# Menampilkan judul-judul dari elemen yang ditemukan
for title in titles:
    print(title.text)
