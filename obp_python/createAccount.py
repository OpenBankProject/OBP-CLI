from .makeRequests import makePutRequest
from .init import get_config


def createAccount(bankid=None, userid=None, currency=None, label=None, productcode=None, branchid=None, accountid=None):

  payload = {
      "user_id": userid,
      "label": label,
      "product_code": productcode,
      "balance": {"currency": currency, "amount": 0},
       "branch_id": branchid,
      "account_routing": {"scheme": "OBP", "address": "4930396"},
      "account_attributes": [
          {"product_code": "saving1", "account_attribute_id": "613c83ea-80f9-4560-8404-b9cd4ec42a7f",
           "name": "OVERDRAFT_START_DATE", "type": "DATE_WITH_DAY", "value": "2012-04-23"}
      ]
  }

  url = get_config('OBP_API_HOST') + '/obp/v4.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}'.format(BANK_ID=bankid, ACCOUNT_ID=accountid)
  
  return makePutRequest(url,payload)
