import requests
import os
import json
from .init import get_config

def createAccount(bankid=None, userid=None, currency=None, label=None, 
                  type=None, balance=None, branchid=None, 
                  accountid=None):

  payload = {
      "user_id": userid,
      "label": label,
      "type": str(type),
      "balance": {
        "currency": currency,
        "amount": balance
      },
      "branch_id": branchid,
      "account_routing": {
        "scheme": "OBP",
        "address": "UK123456"
      }
    }
  
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}'.format(BANK_ID=bankid, ACCOUNT_ID=accountid)
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.put(url, headers=headers, json=payload)

  return req
