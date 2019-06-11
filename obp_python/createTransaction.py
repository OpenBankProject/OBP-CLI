import requests
import os
import json
from .init import get_config

def createTransaction(to_account_id=None, to_bank_id=None, currency=None, 
                amount=None, description=None, 
                challenge_type="SANDBOX_TAN"):

  payload = {
            "to": {
              "account_id": str(to_account_id), 
              "bank_id": to_bank_id
              }, 
            "value": {
              "currency": currency, 
              "amount": amount}, 
            "description": description, 
            "challenge_type" : challenge_type
            }
    
  
  url = get_config('OBP_API_HOST') + '/obp/v1.4.0/banks/{bank_id}/accounts/{to_account_id}/owner/transaction-request-types/{challenge_type}/transaction-requests'.format(bank_id=to_bank_id, to_account_id=to_account_id, challenge_type=challenge_type)
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  return req
