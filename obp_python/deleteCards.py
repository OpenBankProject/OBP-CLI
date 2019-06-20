import requests
import os
import json
from .init import get_config


def deleteCards(bank_id): 
  # Get all cardes
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{}/cardes'.format(bank_id)
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.get(url, headers=headers)
  resp = json.loads(req.text)
  if 'cardes' not in resp:
    return req
  cardes = json.loads(req.text)['cardes']

  ## Delete all cardes
  card_ids = []
  for card in cardes:
    card_ids.append(card['id'])

  for card_id in card_ids:
      url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{}/cardes/{}'.format(bank_id, card_id)
      print(url)
      authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
      headers = {'Content-Type': 'application/json',
                'Authorization': authorization}
      req = requests.delete(url, headers=headers)
      print (req.text)
