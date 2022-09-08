from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()

# use this if you can't run the file from terminal
# after adding this command
# you can run the file
# without having to add FLASK_APP env variable and deal with a bunch of other things

