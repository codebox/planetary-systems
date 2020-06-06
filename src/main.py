from data_source import DataSource
from data_processor import DataProcessor
from svg import Svg
from svg_wrapper import SvgWrapper

planet_data = DataSource().get()
star_data, maxima = DataProcessor(planet_data, 100).get_star_data()
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