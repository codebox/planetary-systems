from field_names import *

DAYS_PER_YEAR = 365

SHOW_MOST_PLANETS = lambda s: -s[PLANET_COUNT]
SHOW_FIRST_DISCOVERED = lambda s: s[PLANET_DISCOVERED]
SHOW_LATEST_DISCOVERIES = lambda s: -s[PLANET_DISCOVERED]

config = {
    'star_count': 100,
    'sort_order': SHOW_FIRST_DISCOVERED,
    'title': 'Planetary Systems',
    'sub_title': 'The First 100 Planetary Systems Discovered by Humanity',
    'out_file': 'planetary-systems.svg',
    'dump_data': True,
    'dump_data_file': 'render_data.json',
    'render_defaults': {
        'orbit_size': 1,
        'planet_radius': 1,
        'planet_orbit_days': DAYS_PER_YEAR
    },
    'download': {
        'csv_file': 'data/exoplanets.csv',
        'url': 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/IceTable/nph-iceTblDownload',
        'post_body': {
            'workspace': '2020.06.05_02.13.37_010518/TblView/2020.06.05_03.57.46_031348',
            'useTimestamp': '1',
            'table': '/exodata/kvmexoweb/ExoTables/planets.tbl',
            'format': 'CSV',
            'user': '',
            'label': '',
            'columns': 'all',
            'rows': 'all',
            'mission': 'ExoplanetArchive',
            'noErrors': 'true'
        }
    },
    'svg': {
        'encoding': 'utf-8',
        'width': 1000,
        'margin_x': 50,
        'margin_y': 100,
        'box_count_x': 10,
        'box_margin_x': 0,
        'box_margin_y': 0,
        'box_padding': 5,
        'box_aspect_ratio': 1.2
    }
}

