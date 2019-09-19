import requests
import os
import json
from .getCardIdByCardNumber import getCardIdByCardNumber
from .init import get_config

def addCardAttribute(bank_id=None, card_number=None,
                    name=None, attribute_type=None,
                    value=None):

  """
  Add a card attribie to a card

  Requires roles: 
  e.g obp addrole --role-name 
  """
  payload = {
    "name": name,
    "type": attribute_type,
    "value": str(value)
  }

  # Work out card id
  card_id = getCardIdByCardNumber(bank_id=bank_id, card_number=card_number)

  url = get_config('OBP_API_HOST') + "/obp/v3.1.0/management/banks/{bank_id}/cards/{card_id}/attribute".format(bank_id=bank_id, card_id=card_id)

  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  
  req = requests.post(url, headers=headers, json=payload)

  return req
