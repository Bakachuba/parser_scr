import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def download(url):
    resp = requests.get(url, stream=True)
    # stream - картинка будет подаваться порционно

    r = open(r'C:\\Users\\Admin\\Desktop\\parser_dir\\' + url.split('/')[-1], 'wb')
    for value in resp.iter_content(1024 * 1024):
        r.write(value)
    r.close()


def get_url():
    for count in range(1, 7):

        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')
        # BS - находит элементы, lxml - фильтрует

        data = soup.find_all("div", class_='w-full rounded border')
        # карточка

        for i in data:
            card_url = 'https://scrapingclub.com' + i.find('a').get('href')
            yield card_url
            # делаем из функции генератор

    # for i in data:
    #     name = i.find('h4').text
    #     # тег имени карточки
    #     price = i.find('h5').text
    #     url_img = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')
    #     out = name + '\n' + price + '\n' + url_img
    #     print(f'page {count} {out}')


# взять информацию с заголовков со всех страниц


def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, 'lxml')
        # BS - находит элементы, lxml - фильтрует

        data = soup.find("div", class_='my-8 w-full rounded border')
        name = data.find('h3', class_='card-title').text
        price = data.find('h4', class_='my-4 card-price').text
        desc = data.find('p', class_='card-description').text

        url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top').get('src')
        download(url_img)
        yield name, price, desc, url_img
