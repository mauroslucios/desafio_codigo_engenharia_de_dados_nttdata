import requests
import json

url = "https://swapi.dev/api/people"

response = requests.get(url, verify=False)

if response.status_code == 200:
    data = response.json()

    with open('response.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("Dados salvos em 'response.json'.")
else:
    print("error, codigo de status", response.status_code)

