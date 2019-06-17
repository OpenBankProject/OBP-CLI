import requests
import os
import json
from .init import get_config
from .answerTransactionChallenge import answerTransactionChallenge

def createTransaction(from_account_id=None, from_bank_id=None, 
                to_account_id=None, to_bank_id=None, currency=None, 
                amount=None, description=None, 
                challenge_type="SANDBOX_TAN"):
  """
  Create a transaction request
  
  If you are wanting to create transactions on behalf of another user,
  then you require the entitlement `canCreateAnyTransactionRequest`.
  
  e.g. using the cli:
  obp addrole --role-name CanCreateAnyTransactionRequest --bank-id <bank-id>
  """
  amount =  float(str(amount).replace(',',''))
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
    
  
  url = get_config('OBP_API_HOST') + '/obp/v2.2.0/banks/{from_bank_id}/accounts/{from_account_id}/owner/transaction-request-types/{challenge_type}/transaction-requests'.format(from_bank_id=from_bank_id, from_account_id=from_account_id, challenge_type=challenge_type)

  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)
 
  if req.status_code is 201: 
    print(req.text)
    # Amounts below 1000 by default complete automatically, 
    # others require accepting/answering the payment request.
    if 'INITIATED' in req.json()['status']:
      # Answer transaction request right away
      transation_req_id=req.json()['id']
      challenge_id =req.json()['challenge']['id']
      req = answerTransactionChallenge(bank_id=to_bank_id, account_id=to_account_id, 
                                  transation_req_id=transation_req_id,
                                  challenge_id=challenge_id)

  return req
