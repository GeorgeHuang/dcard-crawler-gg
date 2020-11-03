from pprint import pprint
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.dcard.tw/f/relationship/p/234699070')
soup = BeautifulSoup(r.text, 'html.parser')
divs = soup.find_all('div', class_='sc-1ghk0k7-0 A-DqzO')
data = {}
#print(divs)
for div in divs:
    name = (div.find('div', class_='sc-7fxob4-4 fbGRfH')).text
    comment = (div.find('div', class_='phqjxq-0 htrzBz')).text
    if name in data:
        data[name].append(comment)
    else:
        data[name] = [comment]

for d in data:
    #print(d, len(data[d]))
    print(d)
    pprint(data[d])
    print('\n')
