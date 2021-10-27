import requests
import json
import re


api_request = requests.get('https://api.coophunter.com/get-app-list')
var = json.loads(api_request.text)


def filtering():
    for i in var['applist']['apps']:
        new_dict_ids = {}
        new_dict_names = {}
        new_dict_ids[i['appid']] = i['appid']
        new_dict_names[i['name']] = i['name']
        dictionary = dict(zip(new_dict_ids, new_dict_names))
        for key, value in dictionary.items():
            if re.search(r'[\u4e00-\u9fff]+', value):
                pass
            else:
                entries = key, value
                with open('data_dump.json', 'a') as data:
                    json.dump(entries, data, indent=4)


filtering()


