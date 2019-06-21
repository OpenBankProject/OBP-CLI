import requests
from .init import get_config
from pyexcel_ods import get_data
import sys, traceback
from .hasEntitlements import hasEntitlements
from .createHistoricalTransaction import createHistoricalTransaction

def importTransactions(spreadsheet=None, sheet_name=None):
  """
  Import transactions from a spreadsheet template
  
  e.g. obp addrole --role-name CanCreateHistoricalTransaction --bank-id gh.29.uk.x
  """

  # Validate entitlements
  requiredEntitlements = ['CanCreateHistoricalTransaction']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)
  
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
      posted = get_value(8, transaction)
      completed = get_value(9, transaction)

      #Post transaction to api
      response = createHistoricalTransaction(from_account_id=from_account_id, 
                                  from_bank_id=from_bank_id, 
                                  to_account_id=to_account_id, 
                                  to_bank_id=to_bank_id, 
                                  currency=currency, amount=amount, 
                                  description=description, 
                                  posted=posted,
                                  completed=completed)

      print(response.text)
      if response.status_code is 201: #Created
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
