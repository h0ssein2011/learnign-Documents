# read file
import json
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
import os

path = '/home/hossein/Desktop/[FreeCoursesOnline.Me] UDACITY - Natural Language Processing Nanodegree v1.0.0/AIND-NLP/data/'
with open(os.path.join(path, 'hieroglyph.txt'), 'r') as f:
    text = f.read()
    print(text)

# read tabular data
df = pd.read_csv(os.path.join(path, 'news.csv'))
df['title'] = df['title'].str.lower()
print(df.head()[['publisher', 'title']])


# get data from json files

r = requests.get('https://quotes.rest/qod.json')
res = r.json()
print(json.dumps(res, indent=4))


# clean data
r = requests.get('https://news.ycombinator.com')
print(r.text)

# Remove HTML tags
# approach 1 with re
pattern = re.compile(r'<.*?>')
r = pattern.sub('', r.text)
print(r)

# approach 2 with bs

# Remove HTML tags using Beautiful Soup library
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.get_text())
