from random import randint

import requests
from bs4 import BeautifulSoup
from time import sleep

payload = {'catId': 445, 'rn': 0, 'rpp': 13}
H = {'Accept-Language':'en-US'}
file = open('auto.csv', 'w', newline='\n')
file.write('Model,Price,Review\n')
url = 'https://www.cars.com/research/luxury/'

while payload['rn']<65:
    resp = requests.get(url, params=payload,  headers=H)
    #print(resp.headers)
    #print(resp)
    content = resp.text
    soup = BeautifulSoup(content, 'html.parser')
    auto = soup.find('div', class_='mlp-listings-container')
    #print(auto)
    auto_all = auto.find_all('div', class_='listingCard')
    for each in auto_all:
        model = each.h4.text
        print(model)
        price = each.find('p', class_='msrp').text
        print(price)
        review = each.find('a', class_='card-stars').text
        print(review)
        file.write(model+','+price+','+review+'\n')

    payload['rn'] += 13
    sleep(randint(15,20))