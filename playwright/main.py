from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


with sync_playwright() as p: 
  browser = p.chromium.launch(headless=False, slow_mo=50)
  page = browser.new_page()
  page.goto('https://lms.smkn4padalarang.sch.id/login/index.php')
  page.fill('input#username', '0058119618')
  page.fill('input#password', '0058119618')
  page.click('button[id=loginbtn]')
  page.is_visible('div.header')
  html = page.inner_html('#page-content')
  soup = BeautifulSoup(html, 'html.parser')
  print(soup.find_all('h2'))
  text = soup.find('h2', {'class': 'd-inline'}).text
  print(f'text = {text}')