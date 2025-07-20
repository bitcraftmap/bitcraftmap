import json
import msgpack

# Read the MessagePack file
with open("caves.msgpack", "rb") as f:
    data = msgpack.unpackb(f.read(), raw=False)  # raw=False to get strings instead of bytes

# Print as pretty JSON
print(json.dumps(data, indent=2))

# Optionally save back to JSON file
with open("check_transformed_caves.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Data unpacked and saved to check_transformed_caves.json")