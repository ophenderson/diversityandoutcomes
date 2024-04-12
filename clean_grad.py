import pandas as pd
import requests

raw = pd.read_excel('Grad Rate 2017-2018.xlsx')
response = requests.get(raw)
