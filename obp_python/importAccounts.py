import requests
import os
import json
from .init import get_config
from pyexcel_ods import get_data
import sys, traceback
import re

def importAccounts(spreadsheet=None, sheet_name=None):
  
  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')
  '''
  Loading location data from ods spreadsheet
  '''
  sheetdata = get_data(spreadsheet).popitem() #Pops first sheet
  accounts = []

  def get_value(index=None, obj=None):
      try:
        return obj[index]
      except IndexError:
        return ''

  for index, account in enumerate(sheetdata[1:][0][1:]): #skips sheetname, and header
    import pdb;pdb.set_trace()
    try:
      username = get_value(0, account)
      label = get_value(1, account)
      account_type = get_value(1, account)
      balance_currency = get_value(3, account)
      balance_amount = 0
      branch_id = get_value(5, account)
      account_routing_scheme = get_value(6, account)
      account_routing_address = get_value(7, account)
      #Build account object
      account = {
        "user_id": "",
        "label": label,
        "type": account_type,
        "balance": {
          "currency": balance_currency,
          "amount": balance_amount
        },
        "branch_id": branch_id,
        "account_routing": {
          "scheme": account_routing_scheme,
          "address": account_routing_address
        }
      }
      accounts.append(account)
    except Exception as e:
      traceback.print_exc(file=sys.stdout)

  #Post accounts to api
  sucessCount = 0
  failCount = 0
  failedBranches = []
  for payload in accounts:
      authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
      headers = {'Content-Type': 'application/json',
                'Authorization': authorization}
      url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{}/accounts'.format(bank_id)
      response = requests.post(url, json=payload, headers=headers)

      print(response.text)
      if response.status_code is not 201:
        print(response.text)
        failCount = failCount + 1
        failedBranches.append(payload)
      elif response.status_code == 201:
        print(response.text)
        sucessCount = sucessCount + 1


  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
  print("The accounts which failed to import, if any,  were:")
  for account in failedBranches:
    print(account)
  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
