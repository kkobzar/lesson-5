import requests
import json
from colorama import Fore, Back, Style

class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.isMen = gender == 'male'


try:

    r = requests.get('https://randomuser.me/api')

    person = json.loads(r.text)
    api_name = person['results'][0]['name']['first']
    api_surname = person['results'][0]['name']['last']
    api_age = person['results'][0]['dob']['age']
    api_gender = person['results'][0]['gender']

    random_person = Person(api_name, api_surname, api_age, api_gender)

    if random_person.isMen:
        print(Fore.BLUE + random_person.name, random_person.surname, random_person.age)
    else:
        print(Fore.MAGENTA + random_person.name, random_person.surname, random_person.age)

except Exception as e:
    print(e)




# try:
#     print('23' / 0)
# except ZeroDivisionError:
#     print('На нуль ділити не можна')
# except TypeError:
#     print('Щось не те з типами')
