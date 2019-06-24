import requests
import os
import json
from .init import get_config
from .hasEntitlements import hasEntitlements

def getCardIdByCardNumber(bank_id=None, card_number=None):
  """
  Get card id by card number.

  Required roles: 
  e.g. obp addrole --role-name --bank-id gh.29.uk.x
  """

  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')


  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}

  # First get all cards at bank (Open Bank Project does not provoide a get
  # card id by card number api call yet
  # https://github.com/OpenBankProject/OBP-API/issues/1328

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/management/banks/{bank_id}/cards'.format(bank_id=bank_id)
  req = requests.get(url, headers=headers)
  if req.status_code != 200: 
    print("ERROR: Could not get all cards")
    print(req.text)
    exit(-1)
  elif req.status_code == 200:
    cards = req.json()['cards']
    # look for card number in cards list & return it
    findCard = [ card for card in cards if card['card_number'] == card_number]
    if len(findCard) == 1:
      return findCard[0]['card_id']
    else:
      return False


  
