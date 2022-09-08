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


# -------------- ERROR 1 ------------ #
# ERROR:
# ps1 cannot be loaded because running scripts is disabled on this system

# SOLUTION
# This could be due to the current user having an undefined ExecutionPolicy.
#
# In PowerShell as Administrator, you could try the following:
#
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

# SOURCE:
# https://stackoverflow.com/questions/41117421/ps1-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system/49112322#49112322
