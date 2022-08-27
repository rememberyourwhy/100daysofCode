import requests

# .get() (url of the endpoint)
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)


# response code signals:
# 1xx: Hold on (Wait)
# 2xx: Here you go (Success)
# 3xx: Go Away (You dont have permission to access this data)
# 4xx: You Screwed Up (Failed)
# 5xx: I Screwed Up (Server's fault, maybe the server was down)

# Some important attribute of response object
# .status_code

# check response code
if response.status_code == 404:
    raise Exception("That resource does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorised to access this data")

# INSTEAD, we can use
response.raise_for_status()
# it will do the same thing with our manual rise commands


data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = [longitude, latitude]
print(iss_position)