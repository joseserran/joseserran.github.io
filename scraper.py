import requests
from bs4 import BeautifulSoup

URL = 'https://elterrat.com/contacto/publico-la-resistencia/'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')



title = soup.find(id='p-header')

print(title)