import json
import msgpack

def generate_claims_json(json_key):

    has_bank = 0
    has_market = 0
    has_waystone = 0

    for building in json_key['buildings']:

        # 985246037 Town Bank
        # 934683282 Town Market
        # 205715693 Waystone
        if building['buildingDescriptionId'] == 985246037:
            has_bank = 1
        if building['buildingDescriptionId'] == 934683282:
            has_market = 1
        if building['buildingDescriptionId'] == 205715693:
            has_waystone = 1

    return {
        '1': json_key['locationX'],
        '2': json_key['locationZ'],
        '3': json_key['name'],
        '4': json_key['tier'],
        '6': json_key['numTiles'],
        '7': json_key['supplies'],
        '8': json_key['updatedAt'],
        '9': has_bank,
        '10': has_market,
        '11': has_waystone,
        '12': json_key['entityId']
    }

### Data from claims.json
with open('assets/data/claims_with_buildings.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

claims_json = [generate_claims_json(key) for key in data]

'''
with open('assets/data/compiled_claims.json', 'w') as file:
    json.dump(claims_json, file)
'''

with open('assets/markers/claims.msgpack', 'wb') as file:
    packed_claims = msgpack.packb(claims_json)
    file.write(packed_claims)