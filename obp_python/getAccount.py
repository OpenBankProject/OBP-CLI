from .makeRequests import makeGetRequest
from .init import get_config

def getAccountById(bank_id=None, account_id=None):
  
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/my/banks/{}/accounts/{}/account'.format(bank_id, account_id)

  return makeGetRequest(url)
