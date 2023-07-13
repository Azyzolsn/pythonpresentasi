import requests 
from bs4 import BeautifulSoup

url = 'https://www.goodreads.com/search?q=love'

r = requests.get(url)

requests = r.content
soup = BeautifulSoup(requests, 'html.parser')

title = soup.findAll('a', attrs={'class' : 'bookTitle'})
author = soup.findAll('a', attrs={'class' : 'authorName'})
rating = soup.findAll('span', attrs={'class' : 'minirating'})

count = 0
for x in range(0, len(title)):
    count += 1
    print("{0}. {1}\nauthor: {2}\nrating: {3}".format(count, title[x].text.strip(), author[x].text.strip(), rating[x].text.strip()))