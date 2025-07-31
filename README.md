## 🗺️
https://bitcraftmap.com

## Things I found

- https://msgpack.org/
- https://geojson.org/
    - https://medium.com/@dmitry.sobolevsky/geojson-tutorial-for-beginners-ce810d3ff169
    - https://leafletjs.com/examples/geojson/
    - https://geojsonlint.com/
- https://h3geo.org/
- https://d3js.org/
    - https://d3-graph-gallery.com/graph/hexbinmap_geo_basic.html
    - https://www.visualcinnamon.com/2013/07/self-organizing-maps-creating-hexagonal/
    - https://www.visualcinnamon.com/2013/07/self-organizing-maps-adding-boundaries/
- https://p5js.org/
- https://docs.mapbox.com/mapbox-gl-js/api/

## Check later
- https://leafletjs.com/plugins.html#layer-switching-controls
- https://github.com/stefanocudini/leaflet-search/tree/master / https://opengeo.tech/maps/leaflet-search/

## Wild ideas board

- Show players on the map dynamically
- Empires borders and watchtowers
- division grid (chunk / regions)
- Region names somewhere
- Calculate player heat density zones
- Get player list of waystone and show on the map the missing waystones
- Lazy loading of data
- Do everything for performace and ease of use
- Show market data for each waypoints
    - Best prices for this market [1/5/10 percentile of prices]
    - Volume of the market calculated in number of orders, total buy order in hexcoins, other methods...
    - Simple links to bitjita market browser




## Pass geoJson with the location.hash

- Possibles attacks : DOS (too many markers) / XSS / Unexpected behavior if malformed string
- https://www.text-utils.com/remove-extra-spaces/
- https://www.base64encode.org/