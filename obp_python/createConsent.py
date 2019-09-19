import requests
import os
import json
from .init import get_config

def createConsent(bank_id=None, consent_type=None, consent_for=None,
                  view='owner', email=None, phone_number=None):
  """Create a consent in Open Bank Project.
  
  Requires entitlements: 
  To add entitlements with cli: `obp addrole --role-name=<role-name>`
  """

  if email is not "" and phone_number is not "":
    print("Invalid usage. Both email and phone_number cannot be set")
    exit(-1)

  if email is "" and phone_number is "":
    print("Invalid usage. Either email or phone_number must be set")
    exit(-1)

  # Determine if create consent request via email or phone_number (SMS)
  if email is not "":
    payload = {
        "for": consent_for,
        "view": view,
        "email": email
    }
  elif phone_number is not "":
    payload = {
        "for": consent_for,
        "view": view,
        "phone_number": phone_number
    }
  

  if email is not "":
    url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/my/consents/EMAIL'.format(bank_id=bank_id)
  if phone_number is not "":
    url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/my/consents/SMS'.format(bank_id=bank_id)
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  if req.status_code == 403:
    print(req.text)
    exit(-1)


  return req
