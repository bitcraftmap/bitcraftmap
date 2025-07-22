import json
import msgpack

def generate_caves_json(json_key):
    if "Cave" not in json_key['name']:
        return None
    
    size = 2 if "Large" in json_key['name'] else 1

    ore_tiers = {
       1: "Ferralith",
       2: "Pyrelite",
       3: "Emarium",
       4: "Elenvar",
       5: "Luminite",
       6: "Rathium",
       7: "Aurumite",
       8: "Celestium",
       9: "Umbracite",
       10: "Astralite"
    }

    for tier_id, tier_name in ore_tiers.items():
        if tier_name in json_key['name']:
            tier = tier_id
            break

    return {
        "1": json_key["location"]["x"] / 23040 * 7676,
        "2": json_key["location"]["z"] / 23040 * 7676,
        "3": size,
        "4": tier
    }

def generate_trees_json(json_key):
    if "Tree" not in json_key['name']: 
        return None
    
    return {
        "1": json_key["location"]["x"] / 23040 * 7676,
        "2": json_key["location"]["z"] / 23040 * 7676
    }

def generate_temples_json(json_key):
    if "Temple" not in json_key['name']:
        return None
    
    return {
        "1": json_key["location"]["x"] / 23040 * 7676,
        "2": json_key["location"]["z"] / 23040 * 7676,
        "3": json_key['name']
    }

def generate_ruined_json(json_key):
    if any(keyword in json_key['name'] for keyword in ["Tree", "Cave", "Temple"]):
        return None
    
    return {
        "1": json_key["location"]["x"] / 23040 * 7676,
        "2": json_key["location"]["z"] / 23040 * 7676,
        "3": json_key['name']
    }


with open("assets/data/caves.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for entry in data:
    transformed = generate_ruined_json(entry)
    if transformed is not None:
        print(transformed)

caves_json = [generate_caves_json(key) for key in data if generate_caves_json(key) is not None]
trees_json = [generate_trees_json(key) for key in data if generate_trees_json(key) is not None]
ruined_json = [generate_ruined_json(key) for key in data if generate_ruined_json(key) is not None]
temples_json = [generate_temples_json(key) for key in data if generate_temples_json(key) is not None]

with open("assets/markers/caves.msgpack", "wb") as file:
    packed_caves = msgpack.packb(caves_json)
    file.write(packed_caves)
with open("assets/markers/trees.msgpack", "wb") as file:
    packed_trees = msgpack.packb(trees_json)
    file.write(packed_trees)
with open("assets/markers/ruined.msgpack", "wb") as file:
    packed_ruined = msgpack.packb(ruined_json)
    file.write(packed_ruined)
with open("assets/markers/temples.msgpack", "wb") as file:
    packed_temples = msgpack.packb(temples_json)
    file.write(packed_temples)