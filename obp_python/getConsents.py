import requests
import os
import json
from .init import get_config

def getConsents(bank_id=None):
  """Get consents of the current user.
  
  Requires entitlements: 
  To add entitlements with cli: `obp addrole --role-name=<role-name>`
  """

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/my/consents'.format(bank_id=bank_id)
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.get(url, headers=headers)

  if req.status_code == 403:
    print(req.text)
    exit(-1)

  return req
