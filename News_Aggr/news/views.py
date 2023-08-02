from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Getting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[2:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



#Getting news from Hindustan times

ix_r = requests.get("https://indianexpress.com/latest-news/")
ix_soup = BeautifulSoup(ix_r.content, 'html5lib')
ix_headings = ix_soup.findAll('h2')
ix_headings = ix_headings[2:]
ix_news = []

for ixn in ix_headings:
    ix_news.append(ixn.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ix_news})
