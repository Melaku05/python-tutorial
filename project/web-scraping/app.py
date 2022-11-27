
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
from bs4 import BeautifulSoup

url = 'https://lazarist.org/'
results = requests.get(url)
tef_soup = BeautifulSoup(results.text, 'html.parser')
tef = tef_soup.find_all('div', class_='full')
for list in tef:
    print(list.text)

# web scraping lists
# url = 'https://lazarist.org/'
# results = requests.get(url)
# tef_soup = BeautifulSoup(results.text, 'html.parser')
# tef = tef_soup.find_all(text='Apply for Admission')
# parent = tef[0].parent
# print(parent)

# web scraping single data
# url = 'https://lazarist.org/'
# results = requests.get(url)
# tef_soup = BeautifulSoup(results.text, 'html.parser')
# tef = tef_soup.find(text='Apply for Admission')
# parent = tef.parent
# print(parent)
