from data_source import DataSource
from data_processor import DataProcessor
from svg import Svg
from svg_wrapper import SvgWrapper

planet_data = DataSource().get()
star_data = DataProcessor(planet_data).get_star_data()

svg = Svg()
svg_wrapper = SvgWrapper(svg)

for star in star_data:
    svg_wrapper.add_star(star)

svg.save('test.svg')