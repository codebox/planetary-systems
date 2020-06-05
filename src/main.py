from data_source import DataSource
from data_processor import DataProcessor

planet_data = DataSource().get()
star_data = DataProcessor(planet_data).get_star_data()
print(star_data)