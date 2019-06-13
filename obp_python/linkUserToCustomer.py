import requests
import os
import json
from .init import get_config

def linkUserToCustomer(bank_id=None, user_id=None, customer_id=None):
  """
  Link User to a Customer

  Requires CanCreateUserCustomerLink OR CanCreateUserCustomerLinkAtAnyBank 
  entitlements
  To get this using OBP cli, do: obp addrole --role-name <role-name>
  """

  payload = {
    "user_id": user_id,  "customer_id": customer_id
    }

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/user_customer_links'.format(bank_id=bank_id)

  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  return req
