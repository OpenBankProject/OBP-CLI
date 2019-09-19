import requests
from .init import get_config
import sys, traceback
from .hasEntitlements import hasEntitlements

#Delete card ( CanDeleteCardsForBank) 

def deleteCardById(bank_id, card_id):
  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')

  # Validate entitlements
  requiredEntitlements = ['CanDeleteCardsForBank']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/management/banks/{bank_id}/cards/{card_id}'.format(bank_id=bank_id, card_id=card_id)

  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.delete(url, headers=headers)

  if req.status_code == 403:
    print(req.text)
    exit(-1)

  return req
