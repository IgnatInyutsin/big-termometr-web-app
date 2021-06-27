import requests

res = requests.get('http://localhost:82/', data={'command': 'site-database-pull'})
print(res.text)