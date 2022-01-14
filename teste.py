import requests

url = "https://api.pipefy.com/graphql"

payload = {"query": "{ pipe (id: 549212) {name}}"}
headers = {
    "authorization": "Bearer YOUR_TOKEN",
    "content-type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)