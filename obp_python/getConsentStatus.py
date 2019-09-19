import requests
import os
import json
from .init import get_config

def getConsentStatus(consent_id=None, certificate=None):
  """Get consent status.
  
  Takes certificate from `obp  obp getconsentstatus --cert example.pem`
  and performs get consent status request, passing the certificate within
  a header called "PSD2-CERT" :S

  Requires entitlements: 
  To add entitlements with cli: `obp addrole --role-name=<role-name>`
  """

  url = get_config('OBP_API_HOST') + '/berlin-group/v1.3/consents/{consent_id}/status'.format(consent_id=consent_id)
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization,
            'PSD2-CERT': certificate.read().rstrip('\n')
            }

  req = requests.get(url, headers=headers)

  if req.status_code == 403:
    print(req.text)
    exit(-1)

  return req
