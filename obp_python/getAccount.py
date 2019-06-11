import requests
from .init import get_config

def getAccountById(bank_id=None, account_id=None):
  
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/my/banks/{}/accounts/{}/account'.format(bank_id, account_id)

  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.get(url, headers=headers)

  return req
