import sys 
sys.path.append('/Users/postkershaw/.pyenv/versions/3.8.5/lib/python3.8/site-packages')


import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import csv
import datetime

csv_date = datetime.datetime.today().strftime("%Y%m%d")

url = 'https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC'

data = pd.read_html(url, header = 0)
	
data[0].head()
data[0].tail()

data[0].to_csv("AAPL_Stock.csv")


















