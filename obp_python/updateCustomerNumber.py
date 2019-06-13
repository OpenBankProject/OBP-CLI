import requests
import os
import json
from .init import get_config

def updateCustomerNumber(bank_id=None, customer_id=None, customer_number=None):
  """
  Update customer number

  """

  payload = {
      "customer_number": customer_number
    }

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/customers/{customer_id}/number'.format(bank_id=bank_id, customer_id=customer_id)

  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  return req
