import requests

res = requests.get('http://tracker.perpetum-mobile.ru:82/', data={'command': 'migration'})
print(res.text)