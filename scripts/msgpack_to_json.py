import json
import msgpack

with open("assets/markers/claims.msgpack", "rb") as file_msgpack:
    data = msgpack.unpackb(file_msgpack.read(), raw=False)

print(json.dumps(data, indent=2))

'''
with open("assets/data/claims.csv.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
'''