import nasdaqdatalink as ndl
import logging
import os

APIKEY = os.getenv('NASDAQ_DATA_LINK_API_KEY')

logging.basicConfig()
data_link_log = logging.getLogger("nasdaqdatalink")
data_link_log.setLevel('DEBUG')


#Retrieving dataset from Nasdaq Data Link

data = ndl.get('NSE/OIL', api_key=APIKEY)
print(data.head())

data =ndl.get('NSE/OIL', start_date='2010-01-01', end_date='2014-01-01', collapse='annual', transformation='rdiff', rows=4, api_key=APIKEY)
print(data.head())



data = ndl.get('WIKI/AAPL', api_key=APIKEY)
print(data.info())
