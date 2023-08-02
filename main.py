import requests
from bs4 import BeautifulSoup

# r = requests.get("https://timesofindia.indiatimes.com/briefs")
# soup = BeautifulSoup(r.content, 'html5lib')
#
# headings = soup.find_all('h2')
#
# headings = headings[2:-13] # removing footer links

# r = requests.get("https://indianexpress.com/latest-news/")
# soup = BeautifulSoup(r.content, 'html5lib')
# newsDivs = soup.findAll('h2')
# for i in newsDivs:
#     print(i.text)
