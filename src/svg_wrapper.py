from field_names import *
from svg_config import *
import random
class SvgWrapper:
    def __init__(self, svg):
        self.svg = svg
        self.star_count = 0
        self.svg.add_styles('.starName', {'font-size': str(SVG_SMALL_TEXT_SIZE) + 'px'})

    def add_star(self, star):
        box_x, box_y, box_w, box_h = self._get_box_for_star(self.star_count)
        self.svg.add_rect(box_x, box_y, box_w, box_h, 'starClass')

        star_disc_width = 2
        system_center_x = box_x + box_w/2
        system_center_y = box_y + box_w/2
        self.svg.add_circle(system_center_x, system_center_y, star_disc_width / 2, 'starDisc')

        for planet in star[PLANETS]:
            orbit_width = random.random() * 40
            self.svg.add_circle(system_center_x, system_center_y, orbit_width/2, 'planetOrbit')

        self.svg.add_centered_text(star[STAR_NAME], box_x + box_w/2, box_y + box_h - SVG_SMALL_TEXT_SIZE, 'starName')
        self.star_count += 1

    def _get_box_for_star(self, star_index):
        box_width = ((SVG_WIDTH - (2 * SVG_MARGIN_X)) / SVG_BOX_COUNT_X) - 2 * SVG_BOX_MARGIN_X
        box_height = box_width * 1.5 #TODO

        box_x = SVG_MARGIN_X + (star_index % SVG_BOX_COUNT_X) * (box_width + 2 * SVG_BOX_MARGIN_X) + SVG_BOX_MARGIN_X
        box_y = SVG_MARGIN_Y + int(star_index / SVG_BOX_COUNT_X) * (box_height + 2 * SVG_BOX_MARGIN_Y) + SVG_BOX_MARGIN_Y

        return box_x, box_y, box_width, box_height
