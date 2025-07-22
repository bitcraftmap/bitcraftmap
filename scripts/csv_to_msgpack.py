import csv
import msgpack

def generate_claims_json(json_key):
    return {
        "1": int(json_key['pos_e']),
        "2": int(json_key['pos_n']),
        "3": json_key['name'],
        "4": json_key['tier']
    }

with open('assets/data/claims.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)

claims_json = [generate_claims_json(key) for key in data]

with open("assets/markers/claims.msgpack", "wb") as file:
    packed = msgpack.packb(claims_json)
    file.write(packed)