from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY= os.getenv("API_KEY")
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'



parameters = {
  'start':5,
  'limit':200,
  'price_min':10,

}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  json_string= json.dumps(data)
 
  
  
  print(json_string)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)