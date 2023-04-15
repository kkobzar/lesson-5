import requests
import json

r = requests.get('https://randomuser.me/api')

person = json.loads(r.text)


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

api_name = person['results'][0]['name']['first']
api_surname = person['results'][0]['name']['last']
api_age = person['results'][0]['dob']['age']


random_person = Person(api_name, api_surname, api_age)

print(random_person.name, random_person.surname, api_age)