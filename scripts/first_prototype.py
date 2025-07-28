import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

def generate_one_chunk_image(json_data, options, color_map):

    fig, ax = plt.subplots(figsize=(16, 16))
    array_32_32 = [json_data['biomes'][i*32:(i+1)*32] for i in range(32)]
    values = np.array(array_32_32)
    
    for row in range(options['chunk_y']):
        for col in range(options['chunk_x']):
            
            # Calculate hex center x, y for pointy-topped hexagons
            x = col * options['hex_width']
            y = row * (options['hex_height'] * 3/4)
            if row % 2 == 1:
                x += options['hex_width'] / 2

            val = values[row, col]
            val = val if val in range(15) else 0
            color = color_map[val]

            hexagon = RegularPolygon(
                (x, y),
                numVertices = 6,
                radius = options['hex_radius'],
                orientation = 0,
                facecolor = color,
                edgecolor = 'none',
                antialiased = False
            )
            ax.add_patch(hexagon)

    # Place any text in the hex maybe useful later
    # ax.text(x, y, str(values[row, col]), ha='center', va='center', fontsize=10)

    # Set limits to avoid trimming
    ax.set_xlim(-options['hex_width'] / 2, options['hex_width'] * (options['chunk_x'] + 0.5))      # Math Sorcery
    ax.set_ylim(-options['hex_radius'], options['hex_height'] * (options['chunk_y'] * 3/4 + 0.25)) # Math Sorcery
    ax.set_aspect('equal')                                        # Makes the aspect ratio of height and width the same
    ax.axis('off')                                                # Remove legend on the sides

    chunk_filename = 'assets/maps/chunks/all/chunk_' + str(json_data['chunk_x']) + '_' + str(json_data['chunk_z']) + '.png'

    plt.savefig(
        chunk_filename,
        dpi = 100,
        bbox_inches = 'tight',
        pad_inches = 0,
        transparent = True
    )
    plt.close(fig)
    plt.close()

hex_radius = 1
options = {
    'chunk_y' : 32,
    'chunk_x' : 32,
    'hex_radius': hex_radius,
    'hex_height': 2 * hex_radius,
    'hex_width': np.sqrt(3) * hex_radius
}

'''
biomes_colors = {
    '0'  : '#FF0000', # Dev
    '1'  : '#404932', # Calm Forest
    '2'  : '#53584b', # Pine Woods
    '3'  : '#b1b1af', # Snowy Peaks
    '4'  : '#616147', # Breezy Grasslands
    '5'  : '#484133', # Autumn Forest
    '6'  : '#615257', # Misty Tundra
    '7'  : '#72674d', # Desert Wasteland
    '8'  : '#354540', # Swamp
    '9'  : '#4c4956', # Rocky Garden
    '10' : '#282f41', # Open Ocean
    '11' : '#656d53', # Safe Meadows
    '12' : '#222222', # Cave
    '13' : '#495943', # Jungle
    '14' : '#473d4c', # Sapwoods
}
'''
biomes_colors = [
    '#FF0000', # Dev
    '#404932', # Calm Forest
    '#53584b', # Pine Woods
    '#b1b1af', # Snowy Peaks
    '#616147', # Breezy Grasslands
    '#484133', # Autumn Forest
    '#615257', # Misty Tundra
    '#72674d', # Desert Wasteland
    '#354540', # Swamp
    '#4c4956', # Rocky Garden
    '#282f41', # Open Ocean
    '#656d53', # Safe Meadows
    '#222222', # Cave
    '#495943', # Jungle
    '#473d4c' # Sapwoods
]
'''
with open('assets/data/terrain_chunk_state/region_7/terrain_chunk_state_new.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for chunk in data:
       generate_one_chunk_image(chunk, options, biomes_colors)

with open('assets/data/terrain_chunk_state/region_8/terrain_chunk_state_new.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for chunk in data:
       generate_one_chunk_image(chunk, options, biomes_colors)

with open('assets/data/terrain_chunk_state/region_9/terrain_chunk_state_new.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for chunk in data:
       generate_one_chunk_image(chunk, options, biomes_colors)
'''

with open('assets/data/terrain_chunk_state/region_4/terrain_chunk_state_new.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for chunk in data:
       generate_one_chunk_image(chunk, options, biomes_colors)

with open('assets/data/terrain_chunk_state/region_5/terrain_chunk_state_new.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for chunk in data:
       generate_one_chunk_image(chunk, options, biomes_colors)

with open('assets/data/terrain_chunk_state/region_6/terrain_chunk_state_new.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for chunk in data:
       generate_one_chunk_image(chunk, options, biomes_colors)

with open('assets/data/terrain_chunk_state/region_1/terrain_chunk_state_new.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for chunk in data:
       generate_one_chunk_image(chunk, options, biomes_colors)

with open('assets/data/terrain_chunk_state/region_2/terrain_chunk_state_new.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for chunk in data:
       generate_one_chunk_image(chunk, options, biomes_colors)

with open('assets/data/terrain_chunk_state/region_3/terrain_chunk_state_new.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for chunk in data:
       generate_one_chunk_image(chunk, options, biomes_colors)