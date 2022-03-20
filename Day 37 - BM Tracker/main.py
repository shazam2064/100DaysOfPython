import requests
from datetime import datetime

USERNAME = "ass-crack-is-uncrackable"
TOKEN = "YouAreAssCrackForever"
GRAPH_ID = "bruh-moments"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "BRUH Moments Graph",
    "unit": "BM",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today = datetime(year=2022, month=1, day=25)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Bruh Moments did you have today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

update_user = "https://pixe.la/@ass-crack-is-uncrackable"

new_user_data = {
    "displayName": "Ass Crack Is Uncrackable",
    "gravatarIconEmail": "gabrielsalomon.990@gmail.com",
    "title": "Professional Bruh'er",
    "timezone": "EST",
    "aboutURL": "https://github.com/shazam2064",
    "pinnedGraphID": GRAPH_ID
}

# response = requests.put(url=update_user, json=new_user_data, headers=headers)
# print(response)
