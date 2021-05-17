import requests

res = requests.get('http://127.0.0.1:82/', data={'command': 'migration'})
print(res.text)