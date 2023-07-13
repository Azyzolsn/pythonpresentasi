import requests
from bs4 import BeautifulSoup

url = "https://www.bukalapak.com/products"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

