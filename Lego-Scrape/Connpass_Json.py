import requests

URL = 'https://connpass.com/api/v1/event/?keyword=python'
r = requests.get(URL)
data = r.json()
for event in data['events']:
    print(event['title'])
