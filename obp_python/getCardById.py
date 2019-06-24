import requests
import os
import json
from .init import get_config
from .hasEntitlements import hasEntitlements

def getCardById(bank_id=None, card_id=None):
  """
  Get card id by card number.

  Required roles: CanGetCardsForBank
  e.g. obp addrole --role-name --bank-id gh.29.uk.x
  """

  # Validate entitlements
  requiredEntitlements = ['CanGetCardsForBank']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)

  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')


  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}

  # First get all cards at bank (Open Bank Project does not provoide a get
  # card id by card number api call yet
  # https://github.com/OpenBankProject/OBP-API/issues/1328

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/management/banks/{bank_id}/cards/{card_id}'.format(bank_id=bank_id, card_id=card_id)
  req = requests.get(url, headers=headers)

  return req


  
