import requests
from .init import get_config

def getEntitlementsCurrentUser():
  
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/my/entitlements'
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.get(url, headers=headers)

  if req.status_code != 200:
    print("ERROR: Could not check current user permissions/entitlements")
    print(req.text)
    exit(-1)

  # Parse current entitlements into list
  entitlements = []

  for entitlement in req.json()['list']:
    entitlements.append(entitlement)

  return entitlements
