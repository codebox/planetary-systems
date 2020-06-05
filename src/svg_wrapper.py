from field_names import *

class SvgWrapper:
    def __init__(self, svg):
        self.svg = svg
        self.star_count = 0

    def add_star(self, star):
        self.svg.add_text(star[STAR_NAME], 50, self.star_count*20, '')
        self.star_count += 1
