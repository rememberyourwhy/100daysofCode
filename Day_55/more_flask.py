from flask import Flask


app = Flask(__name__)


# --------- DECORATORS ------- #
def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


# -------------- FLASK ------------------ #
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World</h1>!' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media1.giphy.com/media/gyRWkLSQVqlPi/' \
           'giphy.gif?cid=ecf05e47oum7fn73janujpi2p' \
           'kamcvxvqvf5lq8mh1xn9ixf&rid=giphy.gif&ct=g" width=200>'


@app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>")
def great(name):
    return f"Hello {name}"


@app.route("/username/<name>/<int:number>")
def great_with_year(name, number):
    return f"Hello {name}, you are {number} years old"


if __name__ == "__main__":
    # app.run(debug=True)
    # debug mode
    app.run()
