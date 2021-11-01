import requests
import json
import re

api_request = requests.get('https://api.coophunter.com/get-app-list')
var = json.loads(api_request.text)


for i in var['applist']['apps']:

    # Create dictionary for appIDs and game titles
    new_dict_ids = {}
    new_dict_names = {}

    # Extracting 'appid' and 'name' from JSON and converting to lists
    new_dict_ids[i['appid']] = i['appid']
    id_list = list(new_dict_ids)

    new_dict_names[i['name']] = i['name']
    names_list = list(new_dict_names)

    # Creating new dictionary
    dictionary = dict(zip(id_list, names_list))

    # Filtering the dictionary to remove entries with Han unicode and create data_dump.json with remaining data
    for key, value in dictionary.items():
        if re.search(r'[\u4e00-\u9fff]+', value):
            pass
        else:
            # with open('data_dump.json', 'w') as data:
            #     json.dump(dictionary, data, indent=4)
            with open('appIDs.txt', 'a', encoding='utf-8') as ids:
                for apps in dictionary.keys():
                    ids.write('https://store.steampowered.com/api/appdetails?appids=' + str(apps) + "\n")

