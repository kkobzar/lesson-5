import requests
import json

r = requests.get('https://randomuser.me/api')

person = json.loads(r.text)

print(person['results'][0]['email'])


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

api_name = person['results'][0]['name']['first']
api_surname = person['results'][0]['name']['last']

print(api_name, api_surname)