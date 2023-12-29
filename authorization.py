from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

work = Session()
# обход куки

work.get('https://quotes.toscrape.com/', headers=headers)

response = work.get('https://quotes.toscrape.com/login', headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

token = soup.find('form').find('input').get('value')

data = {'csrf_token': token, 'username': 'noname', 'password': 'password'}

result = work.post('https://quotes.toscrape.com/login', headers=headers, data=data, allow_redirects=True)

# res = soup.find_all('span', class_='text')
# author = soup.find_all('small', class_='author')
#
#     if len(res) != 0:
#
#     else:
#         break
#остановка скролла страниц