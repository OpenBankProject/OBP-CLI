import requests
import os
import json
from .init import get_config

def addFx(bank_id=None, from_currency=None, to_currency=None, 
          conversion_value=None, inverse_conversion_value=None, 
          effective_date=None):
  """
  Add an exchange rate.

  Requires roles: CanCreateFxRate OR CanCreateFxRateAtAnyBank
  e.g obp addrole --role-name CanCreateFxRateAtAnyBank
  """

  payload = {
    "bank_id": bank_id,
    "from_currency_code": from_currency,
    "to_currency_code": to_currency,
    "conversion_value": float(conversion_value),
    "inverse_conversion_value": float(inverse_conversion_value),
    "effective_date": effective_date
  }

  url = get_config('OBP_API_HOST') + "/obp/v3.1.0/banks/{}/fx".format(bank_id)

  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  
  req = requests.put(url, headers=headers, json=payload)

  return req
