import pandas as pd

url = 'https://docs.python.org/2/library/sqlite3.html'
from_url = pd.read_table(url, sep='\t')
print(from_url.head(3))

