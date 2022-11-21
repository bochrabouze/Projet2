from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json




url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'



parameters = {
  'start':5,
  'limit':200,
  'price_min':10,

}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'd062bf21-faa0-47d8-911d-2ca702703666',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  json_string= json.dumps(data['data'])
 
  
  
  print(json_string)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)