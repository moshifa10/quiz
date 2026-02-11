import requests

ENDPOINT = "https://opentdb.com/api.php"

parameter = {
    "amount": 10,
    "category": 21,
    "type": "boolean"
}

response = requests.get(ENDPOINT,params=parameter)
response.raise_for_status()


data = response.json()
# print(data)

question_data = []

for question in data["results"]:
    question_data.append(question)


# print(question_data)