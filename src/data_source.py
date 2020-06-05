import csv
import os, os.path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

DATA_FILE = 'data/exoplanets.csv'

class DataSource:
    def __init__(self):
        self.data = []

    def get(self):
        if not self.data:
            self._parse_data_file()

        return self.data

    def _parse_data_file(self):
        if not os.path.exists(DATA_FILE):
            self._download_data_file()

        with open(DATA_FILE, 'r') as f:
            self.data = [self._parse_data_file_row(row) for row in csv.DictReader(filter(lambda row: row[0]!='#', f))]

    def _parse_data_file_row(self, row):
        return {
            'name': row['pl_name']
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

