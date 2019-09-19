import requests
import os
import json
from .init import get_config

def answerTransactionChallenge(bank_id=None, account_id=None, transation_req_id=None, 
                challenge_id=None, challenge_type="SANDBOX_TAN"):

    payload = {"id": challenge_id, "answer": "123"}

    url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/accounts/{account_id}/owner/transaction-request-types/SANDBOX_TAN/transaction-requests/{transation_req_id}/challenge'.format(bank_id=bank_id, account_id=account_id, transation_req_id=transation_req_id, challenge_type=challenge_type)
    
    authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
    headers = {'Content-Type': 'application/json',
              'Authorization': authorization}
    req = requests.post(url, headers=headers, json=payload)
    return req
