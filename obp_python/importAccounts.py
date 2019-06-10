import requests
import os
import json
from .init import get_config
from pyexcel_ods import get_data
import sys, traceback
import re
from .createAccount import createAccount

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
  sucessCount = 0
  failCount = 0
  failedAccounts = []

  for index, account in enumerate(sheetdata[1:][0][1:]): #skips sheetname, and header
    try:
      username = get_value(0, account)
      bank_id = get_value(1, account)
      account_id = str(get_value(2, account))
      label = get_value(3, account)
      account_type = get_value(4, account)
      balance_currency = get_value(5, account)
      balance_amount = 0
      branch_id = get_value(7, account)
      account_routing_scheme = get_value(8, account)
      account_routing_address = get_value(9, account)
      # Get user id based on usernamse (NOTE: User must exist in order for 
      # import to succeed). Also, the user making the request must have the 
      # "CanGetAnyUser" entitlement. If you are a super user, you can use
      # `obp addrole --role-name CanGetAnyUser` to grant this entitlement to
      # yourself. 
      authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
      headers = {'Content-Type': 'application/json',
                'Authorization': authorization}
      url = get_config('OBP_API_HOST') + '/obp/v3.1.0/users/username/{USERNAME}'.format(USERNAME=username)
      response = requests.get(url, headers=headers)
      if response.status_code is 200:
        user_id = response.json()['user_id']
      else:
        user_id = 'user not found'

      #Post accounts to api
      response = createAccount(bankid=bank_id, userid=user_id, currency=balance_currency, label=label,
                  type=account_type, balance=balance_amount, branchid=branch_id,
                  accountid=account_id)

      print(response.text)
      if response.status_code is 200:
        print("WARNING: account aleady exists")
        print(response.text)
        sucessCount = sucessCount + 1
      elif response.status_code is 201:
        print(response.text)
        sucessCount = sucessCount + 1
      else:
        print(response.text)
        failCount = failCount + 1
        failedAccounts.append(account)
      
    except Exception as e:
      traceback.print_exc(file=sys.stdout)



  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
  print("The accounts which failed to import, if any,  were:")
  for account in failedAccounts:
    print(account)
  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
