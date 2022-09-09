from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests


app = Flask(__name__)


@app.route("/")
def home():
    random_number = randint(1, 10)
    copyright_year = datetime.now().year
    return render_template(
        "index.html",
        random_number=random_number,
        copyright_year=copyright_year)


@app.route("/guess/<name>")
def guess_name(name):
    more_note = None
    if name == "pt" or name.lower() == "phuongthao":
        age = int(datetime.now().year) - 2003
        gender = "female"
        more_note = "And I think you are very cute"
    else:
        age_response = requests.get(f"https://api.agify.io?name={name}")
        age = age_response.json()["age"]
        gender_response = requests.get(f"https://api.genderize.io?name={name}")
        gender = gender_response.json()["gender"]
    return render_template(
        "guess_by_name.html",
        name=name,
        gender=gender,
        age=age,
        more_note=more_note
    )


@app.route("/blog")
def blog():
    requests_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(requests_url)
    posts = response.json()
    return render_template(
        "blog.html",
        posts=posts,
    )


if __name__ == "__main__":
    app.run(debug=True)

