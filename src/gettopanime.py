from bs4 import BeautifulSoup
import requests

url = "https://anime47.com/"
src = requests.get(url)
src.encoding = 'utf-8'
# print(src.text)
soup = BeautifulSoup(src.text, 'lxml')

# Get titles of top anime
topAnime = soup.findAll('span', class_='list-top-movie-item-vn')
for anime in topAnime:
    print(anime.text) # print title
# print(soup.prettify())