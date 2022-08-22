import json
import pandas
data = pandas.read_csv("data/french_words.csv")
words = {int(index): {
    "French": row.French,
    "English": row.English,
    "known": None
    } for index, row in data.iterrows()
}
data.update(words)
with open("words.json", mode="w") as words_file:
    json.dump(words, words_file, indent=4)

