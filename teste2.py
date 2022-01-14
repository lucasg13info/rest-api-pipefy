import requests

url = "https://api.pipefy.com/graphql"

payload = {"query": "{ pipe (id: 301973598) {testeeeeeee}"}

testeCreacao = {
  "data": {
    "action": "card.create",
    "card": {
      "id": 301973599,
      "pipe_id": "Inbox"
    }
  }
}

headers = {
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDE5MTk5NDAsImVtYWlsIjoibHVjYXMuZXN0ZWZhbm9Ab2kubmV0LmJyIiwiYXBwbGljYXRpb24iOjMwMDEzNjY1Nn19.cik3TIMZz1qY7XgNc90yoXOcJvNGTduSaVxUQZ7vanAI5E5IaglcVkgGyhvsOcApLss2I0FLrX6UGgTwFjnpNg",
    "content-type": "application/json",
    "input": "CreateCardInputt",
    "locations": "Inbox"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)


