#!/usr/bin/env python3

# Below codes from
# https://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup

from bs4 import BeautifulSoup
import requests

url = input("Enter a website to extract the URL's from: ")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
