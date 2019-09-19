import requests
import os
import json
from .init import get_config

def createBank(bank_id=None, full_name=None, short_name=None, 
                logo_url=None, website_url=None, swift_bic=None,
                national_identifier=None, bank_routing_scheme=None,
                bank_routing_address=None):
  """
  Create a bank in Open Bank Project

  Requires role: CanCreateBank
  e.g. obp addrole --role-name CanCreateBank
  """

  payload = {
      "id": bank_id,
      "full_name": full_name, 
      "short_name": short_name,
      "logo_url": logo_url,
      "website_url": website_url,
      "swift_bic": swift_bic,
      "national_identifier": national_identifier,
      "bank_routing":{    
        "scheme": bank_routing_scheme,
        "address": bank_routing_address
      }
    }
  
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks'
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  if req.status_code == 403:
    print(req.text)
    exit(-1)

  return req
