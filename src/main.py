import json
from data_source import DataSource
from data_processor import DataProcessor
from svg import Svg
from svg_wrapper import SvgWrapper
from field_names import *
from config import config

planet_data = DataSource().get()


star_data, maxima = DataProcessor(planet_data, config['star_count'], config['sort_order']).get_star_data()

svg_wrapper = SvgWrapper(Svg(), maxima)

# Save data used to generate SVG - for debugging purposes
if config['dump_data']:
    with open(config['dump_data_file'], 'w') as f:
        f.write(json.dumps(star_data, indent=4))

for star in star_data:
    svg_wrapper.add_star(star)

out_file=config['out_file']
svg_wrapper.save(out_file)
print('Render complete:', out_file)