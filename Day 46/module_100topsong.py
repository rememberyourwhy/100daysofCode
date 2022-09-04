import requests
from bs4 import BeautifulSoup
def get_top_song_list(date):
    billboard_sample_url = "https://www.billboard.com/charts/hot-100/2000-08-12"
    billboard_top_url = "https://www.billboard.com/charts/hot-100"

    billboard_link_with_date = f"{billboard_top_url}/{date}"

    response = requests.get(billboard_link_with_date)
    contents = response.text

    soup = BeautifulSoup(contents, "html.parser")

    top_titles = soup.find_all(name="h3", id="title-of-a-story")
    stripped_top_titles = []

    for title in top_titles:
        raw_text = title.getText()
        stripped_text_list = raw_text.split()
        stripped_text = " ".join(stripped_text_list)
        stripped_top_titles.append(stripped_text)

    only_song_titles = []
    """
    Data Sample after this code:
    Songwriter(s):
    Producer(s):
    Imprint/Promotion Label:
    13 Celebrity Cameo Videos Almost as Weird as That Fake Mark McGrath Breakup One
    Gains in Weekly Performance
    Additional Awards
    Incomplete
    Songwriter(s):
    Producer(s):
    Imprint/Promotion Label:
    Bent
    Songwriter(s):
    Producer(s):
    Imprint/Promotion Label:
    It's Gonna Be Me
    Songwriter(s):
    Producer(s):
    Imprint/Promotion Label:
    Jumpin', Jumpin'
    Songwriter(s):
    """
    for index in range(len((stripped_top_titles)) - 1):
        if stripped_top_titles[index + 1] == "Songwriter(s):":
            new_element = stripped_top_titles[index]
            only_song_titles.append(new_element)

    return only_song_titles
