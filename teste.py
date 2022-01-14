import requests

url = "https://api.pipefy.com/graphql"

payload = {"query": "allCards(pipeId:301973599)"}
#payload = {"query": "{ pipe (id: 301973599) {teste Lucas}}"}
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDE5MTk5NDAsImVtYWlsIjoibHVjYXMuZXN0ZWZhbm9Ab2kubmV0LmJyIiwiYXBwbGljYXRpb24iOjMwMDEzNjY1Nn19.cik3TIMZz1qY7XgNc90yoXOcJvNGTduSaVxUQZ7vanAI5E5IaglcVkgGyhvsOcApLss2I0FLrX6UGgTwFjnpNg",
    "Content-Type": "application/json"
}

#POST
#response = requests.request("POST", url, json=payload, headers=headers)
#print(response.text)


#GET
r = requests.request("GET", url, data=payload)
print(r.text)
#print(requisicao.json())