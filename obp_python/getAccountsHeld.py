from .makeRequests import makeGetRequest
from .init import get_config

def getAccountsHeld(bank_id):
  
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{}/accounts-held'.format(bank_id)

  return makeGetRequest(url)
