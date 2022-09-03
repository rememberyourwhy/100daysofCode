
from bs4 import BeautifulSoup

link = "page.html"
with open(file=link, mode="r") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")

title_tags = soup.find_all("h3", class_="title")

for tag in title_tags[::-1]:
    print(tag.getText())

with open(file="list100.txt", mode="w") as file:
    for tag in title_tags[::-1]:
        writing_value = tag.getText()
        file.write(f"{writing_value}\n")

