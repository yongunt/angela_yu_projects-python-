import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

data = requests.get(URL)

soup = BeautifulSoup(data.text, "html.parser")

movie_titles = soup.findAll("h3", {"class": "title"})

movie_titles.reverse()

with open("movies.txt", mode="w") as title:
    for movie in movie_titles:
        title.writelines(movie.string + "\n")
