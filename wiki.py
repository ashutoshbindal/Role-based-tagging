import wikipedia as wiki
from bs4 import BeautifulSoup
import requests
import sys

search = wiki.search(sys.argv[1])
page = wiki.page(search[0])
url = page.url
url_name = url[::-1].split('/')[0]
url_name = url_name[::-1]
print(page.title)
print(url_name)
print(page.url)

# Extracting using BeautifulSoup
content = requests.get(url).content
soup = BeautifulSoup(content,'lxml')
tag = soup.find('div', {'class' : 'toc'})
links = tag.findAll('a')

# Printing all the section from the Table of Contents
# for link in links:
#     print(link.text)

# Extracting the DBPedia resource page
dbpedia_url = "http://dbpedia.org/page/" + url_name
content = requests.get(dbpedia_url).content
soup = BeautifulSoup(content,'lxml')
#Further processing that may be required for the DBpedia evaluation
# tag = soup.find('div', {'class' : 'toc'})
# links = tag.findAll('a')
