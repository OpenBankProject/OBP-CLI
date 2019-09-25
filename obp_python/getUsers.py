import requests
from .init import get_config
from .hasEntitlements import hasEntitlements
from .makeRequests import makeGetRequest

def getUsers():

  # Validate entitlements
  requiredEntitlements = ['CanGetAnyUser']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/users'
  
  return makeGetRequest(url)
