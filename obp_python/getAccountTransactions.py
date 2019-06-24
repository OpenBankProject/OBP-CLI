import requests
from .init import get_config

def getAccountTransactions(bank_id=None, account_id=None, view_name=None):
  """
  Get transactions for an account.
  """
  
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/accounts/{account_id}/{view_name}/transactions'.format(bank_id=bank_id, account_id=account_id, view_name=view_name)

  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.get(url, headers=headers)

  return req
