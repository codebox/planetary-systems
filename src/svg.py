import codecs
from svg_config import *
from field_names import *

class Svg:
    def __init__(self):
        self.template = open('template.svg').read().replace('%height%', str(SVG_HEIGHT)).replace('%width%', str(SVG_WIDTH))
        self.styles = []
        self.content = []

    def add_styles(self, selector, styles):
        styles_txt = []
        for k, v in styles.items():
            styles_txt.append(u'{0}:{1};'.format(k, v))

        self.styles.append(u'{0}{{{1}}}'.format(selector, ''.join(styles_txt)))

    def add_text(self, text, x, y, style_class):
        self.content.append(u'<text x="{}" y="{}" class="{}">{}</text>'.format(x, y, style_class, text))


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
