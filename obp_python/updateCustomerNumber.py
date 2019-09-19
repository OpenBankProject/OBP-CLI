import requests
import os
import json
from .init import get_config
from .hasEntitlements import hasEntitlements

def updateCustomerNumber(bank_id=None, customer_id=None, customer_number=None):
  """
  Update customer number

  """
  # Validate entitlements
  requiredEntitlements = ['CanUpdateCustomerNumber']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)

  payload = {
      "customer_number": customer_number
    }

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/customers/{customer_id}/number'.format(bank_id=bank_id, customer_id=customer_id)

  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.put(url, headers=headers, json=payload)

  if req.status_code == 400:
    print("WARNING: could not update customer number")
    print(req.text)

  return req
