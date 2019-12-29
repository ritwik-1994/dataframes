import pandas as pd
import re
import requests
import json
from six.moves import urllib
url = 'https://www.kickexam.com/fiverr/skilltest/16/microsoft-excel-test'
from_url = urllib.request.urlopen(url)

fetch = re.findall('Fiverr (\w+)', from_url.read())

print(fetch)

