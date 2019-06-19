import requests
import os
import json
from .init import get_config
from .getCustomerIdByCustomerNumber import getCustomerIdByCustomerNumber
from .hasEntitlements import hasEntitlements

def createCard(bank_id=None, card_number=None, 
                  card_type=None, name_on_card=None, issue_number=None, 
                  serial_number=None, valid_from_date=None, expires_date=None, 
                  enabled=None, technology=None, networks=None, allows=None, 
                  account_id=None, replacement_requested_date=None, 
                  replacement_reason_requested=None, 
                  pin_reset_requested_date=None, 
                  pin_reset_reason_requested=None, collected=None, posted=None, 
                  customer_id=None):
  """Create a card in Open Bank Project.
  
  Requires role: CanCreateCardsForBank
  To add entitlements with cli: `obp addrole --role-name=<role-name>`
  """

  # Validate entitlements
  requiredEntitlements = ['CanCreateCardsForBank', 'CanGetCustomer']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)

  payload = {
    "card_number": card_number,
    "card_type": card_type,  
    "name_on_card": name_on_card,  
    "issue_number": issue_number,  
    "serial_number": serial_number,
    "valid_from_date": valid_from_date,  
    "expires_date": expires_date,
    "enabled": enabled,  
    "technology": technology,  
    "networks": networks.split(','),  
    "allows": allows.split(','),
    "account_id": account_id,  
    "replacement": {    
        "requested_date": replacement_requested_date,
        "reason_requested": replacement_reason_requested  
    },  
    "pin_reset":[
        { 
          "requested_date": pin_reset_requested_date,   
          "reason_requested": pin_reset_reason_requested 
        }
    ],  
    "collected": collected,  
    "posted": posted,  
    "customer_id": customer_id
  }
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/management/banks/{bank_id}/cards'.format(bank_id=bank_id)
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  return req
