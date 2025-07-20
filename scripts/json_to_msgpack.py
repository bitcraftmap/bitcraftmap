import json
import msgpack

def generate_caves_json(json_key):
    name = json_key['name']
    if "Cave" not in name:
        return None
    size = 1 if "Large" in name else 0

    ore_tier = {
        "Ferralith": 1,
        "Pyrelite": 2,
        "Emarium": 3,
        "Elenvar": 4,
        "Luminite": 5,
        "Rathium": 6,
        "Aurumite": 7,
        "Celestium": 8,
        "Umbracite": 9,
        "Astralite": 10
    }

    tier = 0
    for tier_name, id_num in ore_tier.items():
        if tier_name in name:
            tier = id_num
            break

    return {
        "1": tier,
        "2": size,
        "n": json_key["location"]["x"]/23040,
        "e": json_key["location"]["z"]/23040
    }


with open("caves.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for entry in data:
    transformed = generate_caves_json(entry)
    if transformed is not None:
        print(transformed)

caves_json = [generate_caves_json(key) for key in data if generate_caves_json(key) is not None]
with open("caves.msgpack", "wb") as file:
    packed = msgpack.packb(caves_json)
    file.write(packed)