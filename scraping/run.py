import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.goodreads.com/search?q=love'

r = requests.get(url)

requests = r.content
soup = BeautifulSoup(requests, 'html.parser')

title = soup.findAll('a', attrs={'class' : 'bookTitle'})
author = soup.findAll('a', attrs={'class' : 'authorName'})
rating = soup.findAll('span', attrs={'class' : 'minirating'})

# Membuka file CSV untuk menulis
with open('book_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['No.', 'Title', 'Author', 'Rating'])

    count = 0
    for x in range(0, len(title)):
        count += 1
        title_text = title[x].text.strip()
        author_text = author[x].text.strip()
        rating_text = rating[x].text.strip()
        writer.writerow([count, title_text, author_text, rating_text])

print("Data telah berhasil diekspor ke book_data.csv")
