import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "texmex"
TOKEN = "skadjfogidkvfjs490ok"
GRAPH_ID = "commitment"
# /v1/users/<username>/graphs
user_params = {
    "token": TOKEN,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

## Creating account
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Texmex2045",
    "unit": "commit",
    "type": "int",
    "color": "sora",
    "timezone": "Asia/Singapore"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

## Update some params using the put

update_graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# Define the updated parameters
update_params = {
    "name": "Texmex2045", 
    "unit": "commit",      
    "type": "int",         
    "color": "sora",   
}

# response = requests.put(url=update_graph_endpoint, json=update_params, headers=headers)
# print(response.text)


pixel_post_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

posting_params = {
    "date" : "20240722",
    "quantity": "2"
}

response = requests.post(url=pixel_post_endpoint, json=posting_params, headers=headers)
print(response.text)