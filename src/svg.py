import codecs
from svg_config import *
import math

class Svg:
    def __init__(self):
        self.template = open('template.svg').read()
        self.styles = []
        self.content = []

    def add_styles(self, selector, styles):
        styles_txt = []
        for k, v in styles.items():
            styles_txt.append(u'{0}:{1};'.format(k, v))

        self.styles.append(u'{0}{{{1}}}'.format(selector, ''.join(styles_txt)))

    def add_text(self, text, x, y, css_class):
        self.content.append(u'<text x="{}" y="{}" class="{}">{}</text>'.format(x, y, css_class, text))

    def add_centered_text(self, text, x, y, css_class):
        small_font = len(text) > 12
        self.content.append(u'<text x="{}" y="{}" text-anchor="middle" class="{}">{}</text>'.format(x, y, css_class + (' longName' if small_font else ''), text))

    def add_rect(self, x, y, w, h, css_class):
        self.content.append(u'<rect x="{}" y="{}" width="{}" height="{}" class="{}"/>'.format(x, y, w, h, css_class))

    def add_circle(self, x, y, r, css_class):
        self.content.append(u'<circle cx="{}" cy="{}" r="{}" class="{}"/>'.format(x, y, r, css_class))

    def add_circle_segment(self, cx, cy, r, start_angle, end_angle, css_class):
        start_x = cx + r * math.sin(start_angle)
        start_y = cy + r * math.cos(start_angle)
        end_x = cx + r * math.sin(end_angle)
        end_y = cy + r * math.cos(end_angle)
        large_arc = "0" if abs(end_angle - start_angle) < math.pi else "1"
        self.content.append(u'<path d="M {} {} A {} {} 0 {} 0 {} {}" class="{}"/>'.format(start_x, start_y, r, r, large_arc, end_x, end_y, css_class))

    def add_substitutions(self, substitutions):
        for key, value in substitutions.items():
            self.template = self.template.replace('%{}%'.format(key), str(value))

    def save(self, out_file):
        part1, tmp = self.template.split('%style%')
        part2, part3 = tmp.split('%substance%')

        with codecs.open(out_file, 'w', encoding=SVG_ENCODING) as f:
            f.write(part1)
            for style in self.styles:
                f.write(style)
            f.write(part2)
            for content in self.content:
                f.write(content)
            f.write(part3)
