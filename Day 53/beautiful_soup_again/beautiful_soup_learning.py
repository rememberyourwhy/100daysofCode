from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)

# print(soup.title.name)
#
# print(soup.title.string)
#
all_anchor_tags = soup.find_all(name="p")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    tag.get("href")

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", _class="heading")


