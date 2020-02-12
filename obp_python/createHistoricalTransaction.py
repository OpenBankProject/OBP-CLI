import requests
import os
import json
from .init import get_config
from .makeRequests import makePostRequest
from .answerTransactionChallenge import answerTransactionChallenge

def createHistoricalTransaction(from_account_id=None, from_bank_id=None, 
                to_account_id=None, to_bank_id=None, currency=None, 
                amount=None, description=None, posted=None, 
                completed=None):
  """
  Create a historical transaction
  
  Requires entitlement: `CanCreateHistoricalTransaction`.
  
  e.g. using the cli:
  obp addrole --role-name CanCreateHistoricalTransaction 
  """
  amount =  float(str(amount).replace(',',''))
  payload = {
            "from": {
              "bank_id": from_bank_id,
              "account_id": from_account_id 
            },
            "to": {
              "bank_id": to_bank_id,
              "account_id": str(to_account_id)
              },
            "value": {
              "currency": currency, 
              "amount": amount}, 
            "description": description, 
            "posted": str(posted),
            "completed": str(completed),
            "type" : "SANDBOX_TAN",
            "charge_policy": "SHARED"
            }

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/management/historical/transactions'

  return makePostRequest(url,payload)
