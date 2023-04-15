import requests
import json

r = requests.get('https://randomuser.me/api')

person = json.loads(r.text)

print(person['results'][0]['email'])


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
