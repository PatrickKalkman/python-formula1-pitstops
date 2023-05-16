import requests
import json

for round in range(1, 23):
    url = f"https://ergast.com/api/f1/2022/{round}/pitstops.json?limit=1000"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open(f'./pitstops-data/pitstop-2022-{round}.json', 'w') as f:
            json.dump(data, f)
