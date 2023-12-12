import requests
from bs4 import BeautifulSoup as bs
import csv


def write_to_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['img']])
        

def get_html(url):
    response = requests.get(url)
    # print(response.status_code)
    return response.text


def get_data(html):
    soup = bs(html, 'lxml')
    product_list = soup.find_all('div', class_='row')
    # print(product_list)
    for product in product_list:
        title = product.find('div', class_='rows').find('a').text
        
        price = product.find('span', class_='price').text
        # print(price)

        img = product.find('a', class_='product-image-link').find('img').get('src')
        img = 'https://enter.kg' + img 
        # print(img)

        data = {
            'title': title,
            'price': price,
            'img': img
        }
        write_to_csv(data)



def main():
    url = 'https://enter.kg/computers/noutbuki_bishkek'
    html = get_html(url)
    get_data(html)

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['title      ', 'price     ', 'image     '])

main()