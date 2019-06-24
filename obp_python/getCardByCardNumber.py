import requests
import os
import json
from .init import get_config
from .getCardIdByCardNumber import getCardIdByCardNumber
from .getCardById import getCardById

def getCardByCardNumber(bank_id=None, card_number=None):
  """
  Get card by card number.

  """

  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')


  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}

  # First get card_id by card number
  # (Open Bank Project does not provide get card by card number api call yet)
  card_id = getCardIdByCardNumber(bank_id=bank_id, card_number=card_number)

  req = getCardById(bank_id=bank_id, card_id=card_id)
  if req is False:
    print("ERROR: Could not locate a card with number: {}".format(card_number))
  if req.status_code != 200: 
    print("ERROR: Could not get card. Number: '{}', Id: '{}'".format(card_number, card_id ))
    print(req.text)
    exit(-1)
  elif req.status_code == 200:
    return req


  
