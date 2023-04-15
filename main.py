import requests

help(requests)
r = requests.get('https://randomuser.me/api')

print(r.content)
pers = r.content
