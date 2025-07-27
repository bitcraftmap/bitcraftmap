# Goal is to reduce chunk data to the minimum

'''
'chunk_index': 196132,
'chunk_x''"': 131,
'chunk_z': 196,
'dimension': 1,
'biomes': [1,1,1,1,1,1,1,1,1,1
'elevations': [25,25,25,25,25,
'water_levels': [0,0,0,0,0,0,0
'water_body_types': [0,0,0,0,0
'zoning_types': [0,0,0,0,0,0,0
'original_elevations': [25,25,
'''

# remove : original_elevations, elevations, zoning_types, water_levels,
# remove all 0 0 chunks ? real 0 0 will be missing

import json

chunk_data_file = 'assets/data/terrain_chunk_state/region_3/terrain_chunk_state.json'
chunk_data_file_new = 'assets/data/terrain_chunk_state/region_3/terrain_chunk_state_new.json'

remove_keys = ['elevations', 'water_levels', 'zoning_types', 'original_elevations', 'chunk_index', 'dimension']

def remove_keys_from_dict(d, keys_to_remove):
    if isinstance(d, dict):
        return {k: remove_keys_from_dict(v, keys_to_remove) 
                for k, v in d.items() if k not in keys_to_remove}
    elif isinstance(d, list):
        return [remove_keys_from_dict(item, keys_to_remove) for item in d]
    else:
        return d


with open(chunk_data_file, 'r') as file:
    data = json.load(file)

new_json = remove_keys_from_dict(data, remove_keys)

with open(chunk_data_file_new, 'w') as file:
    json.dump(new_json, file)