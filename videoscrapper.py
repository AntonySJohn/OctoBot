from requests import get
from bs4 import BeautifulSoup

def videoScrapper(URL):
  response = get(URL)
  soup = BeautifulSoup(response.content, 'html5lib').find('video')
  print(soup.prettify())
  return soup.find('source')['src']