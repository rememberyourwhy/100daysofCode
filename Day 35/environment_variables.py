import os

# to get it from venv, first we have to export the key
# export OWM_API_KEY=8dc1a372b6d8c125d3f718a9b1457da9 in the console, or the terminal
# check the list using env
# api_key = os.environ.get("OWM_API_KEY")
# print(os.environ["YOUR_VAR"])

# activate: venv\Scripts\Activate.ps1


# the other way is to Edit Configurations
test = os.environ.get("TEST")
print(test)
