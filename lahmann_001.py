import pandas as pd
import requests
from zipfile import ZipFile
#salaries = pd.read_csv('/home/shipsy/Downloads/baseballdatabank-2019.2/core/Salaries.Csv')
#teams = pd.read_csv('/home/shipsy/Downloads/baseballdatabank-2019.2/core/Teams.Csv')

r = requests.get('http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip')
print(r.headers['content-type'])

