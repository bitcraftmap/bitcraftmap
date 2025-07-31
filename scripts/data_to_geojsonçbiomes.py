import numpy as np
from skimage import measure
from shapely.geometry import Polygon, mapping
import json

# Suppose `biome_data` is a 2D numpy array of shape (7680, 7680)
# Each element is a biome label (int or str)

biome_data = []
geojson_features = []


for biome_type in np.unique(biome_data):
    mask = (biome_data == biome_type)

    # Label connected regions
    labeled, num = measure.label(mask, connectivity=1, return_num=True)

    for region_label in range(1, num + 1):
        region_mask = (labeled == region_label)

        # Find contours (note: returns coords in (row, col))
        contours = measure.find_contours(region_mask, level=0.5)

        for contour in contours:
            # Flip to (x, y) format if needed
            coords = [(float(x), float(y)) for y, x in contour]

            polygon = Polygon(coords)

            if not polygon.is_valid or polygon.area < 10:  # Skip small or invalid
                continue

            feature = {
                "type": "Feature",
                "properties": {"biome": str(biome_type)},
                "geometry": mapping(polygon)
            }

            geojson_features.append(feature)

geojson = {
    "type": "FeatureCollection",
    "features": geojson_features
}

# Save to file
with open("biomes.geojson", "w") as f:
    json.dump(geojson, f)