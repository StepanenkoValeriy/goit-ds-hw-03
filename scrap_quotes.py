import requests
from bs4 import BeautifulSoup
import json


url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes_data = []
authors_data = []
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('div', class_='quote')
tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    quote_text = quotes[i].text
    author_fullname = authors[i].text
    tags_list = [tag.text for tag in tags[i].find_all('a', class_='tag')]

    quote_info = {
        'text': quote_text,
        'author': author_fullname,
        'tags':tags_list
        } 
    quotes_data.append(quote_info)

with open('quotes.json', 'w') as quotes_file:
    json.dump(quotes_data, quotes_file, indent=4)

for author in authors:
    author_fullname = author.find('small', class_='author').text
    author_page_url = url + author.find('a')['href']  
    author_page_response = requests.get(author_page_url)
    author_page = BeautifulSoup(author_page_response.text, 'html.parser')
    born_date = author_page.find('span', class_='author-born-date').text.strip()
    born_location = author_page.find('span', class_='author-born-location').text.strip()
    description = author_page.find('div', class_='author-description').text.strip()

    author_fullnames = {
        'fullname': author_fullname,
        'born_date': born_date,
        'born_location': born_location,
        'description': description
        }
    authors_data.append(author_fullnames)

with open('authors.json', 'w') as authors_file:
    json.dump(authors_data, authors_file, indent=4)