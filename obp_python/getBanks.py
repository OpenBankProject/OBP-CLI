from .makeRequests import makeGetRequest
from .init import get_config

def getBanks():
  
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks'

  return makeGetRequest(url)
