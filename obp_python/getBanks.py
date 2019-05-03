import requests
import os
import json
from .init import get_config

def getBanks():
  
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks'
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.get(url, headers=headers)

  return req
