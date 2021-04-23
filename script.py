from bs4 import BeautifulSoup
from requests import get

class GameLink:
    pageNumber = 1
    URL = f"https://octocurio.com/category/games/indie-games/page/{pageNumber}/"
    def nextPage(self):
        self.pageNumber+=1
        self.URL = f"https://octocurio.com/category/games/indie-games/page/{self.pageNumber}/"
