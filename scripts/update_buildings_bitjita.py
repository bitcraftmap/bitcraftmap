import requests
import json
import time

user_agent = {'User-agent': 'Manserk For bitcraftmap.com'}
bitjita_url = 'https://bitjita.com/api/claims/'

def query_buildings_from_entityid(entityid):

    time.sleep(1)
    buildings_endpoint = bitjita_url + str(entityid) + '/buildings'
    print('Requesting ' + buildings_endpoint)
    return requests.get(buildings_endpoint, user_agent).json()

with open('assets/data/claims.json', 'r') as file:
    data = json.load(file)

claims_with_buildings = []
count = len(data)
print('There are ' + str(count) + ' claims in the list of claims file')
for claim in data:
    print(str(count) + ' left to do')
    claim['buildings'] = query_buildings_from_entityid(claim['entityId'])
    claims_with_buildings.append(claim)
    count -= 1


print('There are ' + str(len(claims_with_buildings)) + ' claims in the json with buildings file')

with open("assets/data/claims_with_buildings.json", "w") as file:
    json.dump(claims_with_buildings, file)