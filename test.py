from bs4 import BeautifulSoup
from requests import get
#from script import GameLink

response = get("https://octocurio.com/category/games/indie-games/page/122/")

soup = BeautifulSoup(response.content,'html5lib')

articles = soup.find_all('article')
print(len(articles))

for article in articles:
  print(article.find('a')['href'])