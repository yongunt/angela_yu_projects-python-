from bs4 import BeautifulSoup
import requests
import lxml

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "lxml")
#
# print(soup.select("ul"))
#


response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

my_anchors = soup.find_all("a", {"class": "titlelink"})
myRanks = soup.find_all("span", {"class": "rank"})

for (rank, title, href) in zip(myRanks, my_anchors, my_anchors):
    print(rank.string, title.string + "\n" + href.get("href") + "\n")

# a = 1
# for anchor in my_anchors:
#     print(str(a) + "." + anchor.string)
#     a += 1
