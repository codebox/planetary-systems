from field_names import *

class DataProcessor:
    def __init__(self, planet_data):
        self.planet_data = planet_data
        self.star_data = {}

    def get_star_data(self):
        for planet in self.planet_data:
            star_name = planet[STAR_NAME]

            if star_name not in self.star_data:
                star = self.star_data[star_name] = self._build_star_data(planet)

            else:
                star = self.star_data[star_name]
                assert star[STAR_TYPE] == planet[STAR_TYPE]
                assert star[STAR_RADIUS] == self._to_float(planet[STAR_RADIUS])
                assert star[STAR_DISTANCE] == self._to_float(planet[STAR_DISTANCE])
                assert star[STAR_MAGNITUDE] == self._to_float(planet[STAR_MAGNITUDE])
                assert star[PLANET_COUNT] == int(planet[PLANET_COUNT])

            star[PLANETS].append(self._build_planet_data(planet))

        for star_name, star_data in self.star_data.items():
            assert len(star_data[PLANETS]) == star_data[PLANET_COUNT], 'Planet count mismatch for star "{}", data was {}'.format(star_name, star_data)

        return self.star_data

    def _build_star_data(self, planet):
        return {
            STAR_TYPE: planet[STAR_TYPE],
            STAR_RADIUS: self._to_float(planet[STAR_RADIUS]),
            STAR_DISTANCE: self._to_float(planet[STAR_DISTANCE]),
            STAR_MAGNITUDE: self._to_float(planet[STAR_MAGNITUDE]),
            PLANETS: [],
            PLANET_COUNT: int(planet[PLANET_COUNT])
        }

    def _build_planet_data(self, planet):
        return {
            PLANET_NAME: planet[PLANET_NAME],
            PLANET_DISCOVERED: int(planet[PLANET_DISCOVERED]),
            PLANET_RADIUS: self._to_float(planet[PLANET_RADIUS]),
            PLANET_ORBIT_SIZE: self._to_float(planet[PLANET_ORBIT_SIZE]),
            PLANET_ORBIT_DAYS: self._to_float(planet[PLANET_ORBIT_DAYS])
        }

    def _to_float(self, value):
        return float(value) if value else None