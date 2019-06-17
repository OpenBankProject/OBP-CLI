import requests
from .init import get_config
from pyexcel_ods import get_data
import sys, traceback
from .createTransaction import createTransaction

def importTransactions(spreadsheet=None, sheet_name=None):
  """
  Import transactions from a spreadsheet template

  Creates and auto-accepts transaction reqests against 
  the account(s) specified in the template.
  
  If importing transactions against accounts which are not
  owned by your account, then you require the permission: 
  canCreateAnyTransactionRequest

  e.g. obp addrole --role-name CanCreateAnyTransactionRequest --bank-id gh.29.uk.x
  """
  
  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')
  '''
  Loading location data from ods spreadsheet
  '''
  sheetdata = get_data(spreadsheet).popitem() #Pops first sheet
  transactions = []

  def get_value(index=None, obj=None):
      try:
        return obj[index]
      except IndexError:
        return ''
  sucessCount = 0
  failCount = 0
  failedTransactions = []

  for index, transaction in enumerate(sheetdata[1:][0][1:]): #skips sheetname, and header
    try:
      from_account_id = get_value(0, transaction)
      from_bank_id = get_value(1, transaction)
      to_account_id = get_value(2, transaction)
      to_bank_id = get_value(3, transaction)
      currency = get_value(4, transaction)
      amount = get_value(5, transaction)
      description = get_value(6, transaction)
      challenge_type = get_value(7, transaction)

      #Post transaction to api
      response = createTransaction(from_account_id=from_account_id, 
                                  from_bank_id=from_bank_id, 
                                  to_account_id=to_account_id, 
                                  to_bank_id=to_bank_id, 
                                  currency=currency, amount=amount, 
                                  description=description, 
                                  challenge_type=challenge_type)

      print(response.text)
      if response.status_code is 201 or response.status_code is 202:
        # 201 means transaction was accepted (less than 1000 by default always
        # accepted
        # 202 means he request has been accepted for processing, and an 
        # automated attempt will be made to accept the request. 
        # TODO surface the sucess of a 202 response to the cli output
        print(response.text)
        sucessCount = sucessCount + 1
      else:
        print(response.text)
        failCount = failCount + 1
        failedTransactions.append(transaction)
      
    except Exception as e:
      traceback.print_exc(file=sys.stdout)



  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
  print("The transactions which failed to import, if any,  were:")
  for transaction in failedTransactions:
    print(transaction)
  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
