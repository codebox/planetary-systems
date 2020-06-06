from data_source import DataSource
from data_processor import DataProcessor
from svg import Svg
from svg_wrapper import SvgWrapper
from field_names import *

planet_data = DataSource().get()

SHOW_MOST_PLANETS = lambda s: -s[PLANET_COUNT]
SHOW_FIRST_DISCOVERED = lambda s: int(s[PLANET_DISCOVERED].replace('-',''))
SHOW_LATEST_DISCOVERIES = lambda s: -int(s[PLANET_DISCOVERED].replace('-',''))

star_data, maxima = DataProcessor(planet_data, 100, SHOW_FIRST_DISCOVERED).get_star_data()
svg = Svg()
svg_wrapper = SvgWrapper(svg, maxima)

import json
with open('render_data.json', 'w') as f:
    f.write(json.dumps(star_data, indent=4))

for star in star_data:
    svg_wrapper.add_star(star)

OUT_FILE='exoplanets.svg'
svg.save(OUT_FILE)
print('Render complete:', OUT_FILE)