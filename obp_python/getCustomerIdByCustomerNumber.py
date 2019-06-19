import requests
import os
import json
from .init import get_config
from .hasEntitlements import hasEntitlements

def getCustomerIdByCustomerNumber(customer_number=None, bank_id=None):
  """
  Get customer id by customer number.

  Required roles: CanGetCustomer
  e.g. obp addrole --role-name CanCreateCardsForBank --bank-id gh.29.uk.x
  """

  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')

  # Validate entitlements
  requiredEntitlements = ['CanGetCustomer']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)

  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}

  payload = { "customer_number": customer_number }

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/customers/customer-number'.format(bank_id=bank_id,
            customer_number=customer_number)
  req = requests.post(url, headers=headers, json=payload)
  #BUG obp api returns 201 for this api call but should be 200
  # https://github.com/OpenBankProject/OBP-API/issues/1326
  if req.status_code != 201: 
    print(req.text)
    exit(-1)
  return req
