from field_names import *
from config import config, DAYS_PER_YEAR

class DataProcessor:
    def __init__(self, planet_data, count, get_sort_key):
        self.planet_data = planet_data
        self.star_data = []
        self.count = count
        self.get_sort_key = get_sort_key
        self.maxima = None

    def get_star_data(self):
        if not self.star_data:
            star_data_lookup = {}

            for planet in self.planet_data:
                star_name = planet[STAR_NAME]

                if star_name not in star_data_lookup:
                    star = star_data_lookup[star_name] = self._build_star_data(planet)

                else:
                    star = star_data_lookup[star_name]
                    assert star[STAR_NAME] == planet[STAR_NAME]
                    assert star[STAR_TYPE] == planet[STAR_TYPE]
                    assert star[STAR_RADIUS] == self._to_float(planet[STAR_RADIUS])
                    assert star[STAR_DISTANCE] == self._to_float(planet[STAR_DISTANCE])
                    assert star[STAR_MAGNITUDE] == self._to_float(planet[STAR_MAGNITUDE])
                    assert star[PLANET_COUNT] == int(planet[PLANET_COUNT])

                star[PLANETS].append(self._build_planet_data(planet))

            for name, data in star_data_lookup.items():
                assert len(data[PLANETS]) == data[PLANET_COUNT], 'Planet count mismatch for star "{}", data was {}'.format(name, data)
                data[PLANET_DISCOVERED] = min(map(lambda p: p[PLANET_DISCOVERED], data[PLANETS]))

            star_data = list(star_data_lookup.values())
            star_data.sort(key=self.get_sort_key)
            star_data=star_data[:self.count]

            self.star_data = star_data
            self.maxima = self._calculate_maxima(star_data)

        return self.star_data, self.maxima

    def _calculate_maxima(self, all_star_data):
        max_star_radius = -1
        max_planet_radius = -1
        max_orbit_radius = -1

        for star_data in all_star_data:
            max_star_radius = max(max_star_radius, star_data[STAR_RADIUS] or 0)

            for planet in star_data[PLANETS]:
                max_planet_radius = max(max_planet_radius, planet[PLANET_RADIUS] or 0)
                max_orbit_radius = max(max_orbit_radius, planet[PLANET_ORBIT_SIZE] or 0)

        return {
            STAR_RADIUS: max_star_radius,
            PLANET_RADIUS: max_planet_radius,
            PLANET_ORBIT_SIZE: max_orbit_radius
        }

    def _build_star_data(self, planet):
        return {
            STAR_NAME: planet[STAR_NAME],
            STAR_TYPE: planet[STAR_TYPE],
            STAR_RADIUS: self._to_float(planet[STAR_RADIUS]),
            STAR_DISTANCE: self._to_float(planet[STAR_DISTANCE]),
            STAR_MAGNITUDE: self._to_float(planet[STAR_MAGNITUDE]),
            PLANETS: [],
            PLANET_COUNT: int(planet[PLANET_COUNT])
        }

    def _build_planet_data(self, planet):
        render_defaults = config['render_defaults']
        return {
            PLANET_NAME: planet[PLANET_NAME],
            PLANET_DISCOVERED: int(planet[PLANET_DISCOVERED]),
            PLANET_RADIUS: self._to_float(planet[PLANET_RADIUS]) or render_defaults['planet_radius'],
            PLANET_ORBIT_SIZE: self._to_float(planet[PLANET_ORBIT_SIZE]) or render_defaults['orbit_size'],
            PLANET_ORBITS_PER_YEAR: DAYS_PER_YEAR / self._to_float(planet[PLANET_ORBIT_DAYS], render_defaults['planet_orbit_days'])
        }

    def _to_float(self, value, default_value=None):
        return float(value) if value else default_value
