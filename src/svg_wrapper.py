from field_names import *
from svg_config import *
import math

class SvgWrapper:
    def __init__(self, svg, maxima):
        self.svg = svg
        self.maxima = maxima
        self.star_count = 0
        self.svg.add_styles('.starName', {'font-size': str(SVG_SMALL_TEXT_SIZE) + 'px'})
        self.box_width = ((SVG_WIDTH - (2 * SVG_MARGIN_X)) / SVG_BOX_COUNT_X) - 2 * SVG_BOX_MARGIN_X
        self.box_height = self.box_width * 1.5 #TODO

        self._rescale_orbit = self._build_log_rescale(0, maxima[PLANET_ORBIT_SIZE], 5, self.box_width/2 - SVG_BOX_PADDING)
        self._rescale_star_width = self._build_log_rescale(0, maxima[STAR_RADIUS], 5, 10)

    def add_star(self, star):
        box_x, box_y = self._get_box_for_star(self.star_count)
        self.svg.add_rect(box_x, box_y, self.box_width, self.box_height, 'starBox')

        star_disc_width = self._rescale_star_width(star[STAR_RADIUS] or 0)
        system_center_x = box_x + self.box_width/2
        system_center_y = box_y + self.box_width/2
        self.svg.add_circle(system_center_x, system_center_y, star_disc_width / 2, 'starDisc starDisc' + (star[STAR_TYPE] or 'O')[0])

        for planet in star[PLANETS]:
            if planet[PLANET_ORBIT_SIZE]:
                orbit_radius = self._rescale_orbit(planet[PLANET_ORBIT_SIZE])
                self.svg.add_circle(system_center_x, system_center_y, orbit_radius, 'planetOrbit')

        self.svg.add_centered_text(star[STAR_NAME], box_x + self.box_width/2, box_y + self.box_height - SVG_SMALL_TEXT_SIZE, 'starName')
        self.star_count += 1

    def _build_log_rescale(self, orig_min, orig_max, scaled_min, scaled_max):
        log_min = math.log(1+orig_min)
        log_max = math.log(1+orig_max)
        scaled_range = scaled_max - scaled_min

        def log_rescale(value):
            log_value = math.log(1+value)
            return scaled_min + scaled_range * (log_value - log_min)/(log_max - log_min)

        return log_rescale

    def _get_box_for_star(self, star_index):
        box_x = SVG_MARGIN_X + (star_index % SVG_BOX_COUNT_X) * (self.box_width + 2 * SVG_BOX_MARGIN_X) + SVG_BOX_MARGIN_X
        box_y = SVG_MARGIN_Y + int(star_index / SVG_BOX_COUNT_X) * (self.box_height + 2 * SVG_BOX_MARGIN_Y) + SVG_BOX_MARGIN_Y

        return box_x, box_y

    def _get_color_from_type(self, star_type):
        star_class = star_type[0]
        return COLOUR_LOOKUP.get(star_class, 'O')


