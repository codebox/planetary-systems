import csv
import os, os.path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from field_names import *

DATA_FILE = 'data/exoplanets.csv'

class DataSource:
    def __init__(self):
        self.data = []

    def get(self):
        if not self.data:
            self._parse_data_file()
            self._add_solar_system_data()

        return self.data

    def _parse_data_file(self):
        if not os.path.exists(DATA_FILE):
            self._download_data_file()

        with open(DATA_FILE, 'r') as f:
            self.data = [self._parse_data_file_row(row) for row in csv.DictReader(filter(lambda row: row[0]!='#', f))]

    def _parse_data_file_row(self, row):
        return {
            PLANET_NAME: row['pl_name'],
            STAR_NAME: row['pl_hostname'],
            PLANET_COUNT: row['pl_pnum'],
            PLANET_ORBIT_DAYS: row['pl_orbper'],
            PLANET_ORBIT_SIZE: row['pl_orbsmax'],
            STAR_DISTANCE: row['st_dist'],
            STAR_MAGNITUDE: row['st_optmag'],
            STAR_RADIUS: row['st_rad'],
            PLANET_RADIUS: row['pl_rade'],
            PLANET_DISCOVERED: (row['pl_publ_date'] or row['pl_disc'] + '-01').replace('-', ''),
            STAR_TYPE: row['st_spstr']
        }

    def _download_data_file(self):
        url = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/IceTable/nph-iceTblDownload'

        post_fields = {
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

        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        print('Downloading data from {}...'.format(url))
        request = Request(url, urlencode(post_fields).encode())
        with open(DATA_FILE,'w') as f:
            csv_data = urlopen(request).read().decode()
            f.write(csv_data)
        print('Download complete')

    def _add_solar_system_data(self):
        def build_planet_data(name, orbit_days, orbit_size, radius, discovered):
            return {
                PLANET_NAME: name,
                STAR_NAME: 'Sol',
                PLANET_COUNT: 8,
                PLANET_ORBIT_DAYS: orbit_days,
                PLANET_ORBIT_SIZE: orbit_size,
                STAR_DISTANCE: 0.000004848,
                STAR_MAGNITUDE: -26.74,
                STAR_RADIUS: 1,
                PLANET_RADIUS: radius,
                PLANET_DISCOVERED: discovered,
                STAR_TYPE: 'G2'
            }

        self.data.append(build_planet_data('Mercury', 88, 0.387, 0.382, 0))
        self.data.append(build_planet_data('Venus', 224, 0.72, 0.949, 0))
        self.data.append(build_planet_data('Earth', 365, 1, 1, 0))
        self.data.append(build_planet_data('Mars', 687, 1.513, 0.532, 0))
        self.data.append(build_planet_data('Jupiter', 4331, 5.187, 11.209, 0))
        self.data.append(build_planet_data('Saturn', 10747, 9.553, 9.449, 0))
        self.data.append(build_planet_data('Uranus', 30589, 19.147, 4.007, 178103))
        self.data.append(build_planet_data('Neptune', 90560, 29.967, 3.883, 184609))

