#! /bin/python3

import requests
import sys
from bs4 import BeautifulSoup 

word = sys.argv[1]
url = f'https://www.google.com/search?q={word}&hl=en&tbm=isch' 

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

try:
    print(soup.find_all('img')[2]['src'])
except:
    print('No image found')
