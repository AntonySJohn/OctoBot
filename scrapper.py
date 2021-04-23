from requests import get
from bs4 import BeautifulSoup
from videoscrapper import videoScrapper
from script import GameLink

gameLink = GameLink()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# response = get(url=gameLink.URL, headers=headers)
# soup = BeautifulSoup(response.content,'html5lib')
# articles = soup.find_all('article')
file = open('text.txt','w')
for _ in range(122):
  response = get(url=gameLink.URL, headers=headers)
  soup = BeautifulSoup(response.content,'html5lib')
  articles = soup.find_all('article')
  for article in articles:
    file.write(article.find('a')['href'])
    file.write("\n")
  print(gameLink.pageNumber)
  gameLink.nextPage()
  
# for test in articles:
#   print(test.prettify())
#   break
  #print(test.find('a')['href'])
# for article in soup.find_all('article'):
#   print(videoScrapper(article.find('iframe')['data-src']))
# videoURL = articles.find('iframe')['data-src']
# videoScrapper(videoURL)
# print(articles.prettify())
# print(videoScrapper(videoURL))
