import requests
from requests.exceptions import HTTPError

urls = open('appIDs.txt', 'r')


try:
    with urls as f:
        url = f.readline()
        response = requests.get(url)
        response.raise_for_status()
        json_response = response.json()
        print(json_response)
except HTTPError as http_err:
    print(f'An HTTP error has occurred: {http_err}')
except Exception as err:
    print(f'Another error has occurred: {err}')


for key, value in json_response.items():
    categories = json_response[key]['data']['categories']
    for k in categories:
        description = k['description']
        try:
            if description == 'Single-player':
                print('This isn\'t co-op friendly')
            else:
                print('This is a co-op game!')
        except description == 'Single player' as err:
            print(f'This is not co-op friendly')

