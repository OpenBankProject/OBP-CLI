import requests
from .init import get_config
from .getEntitlementsCurrentUser import getEntitlementsCurrentUser

def hasEntitlements(entitlements_required=[]):
  """
  Check current user has entitlements
  
  Returns: 
    - fail (bolean)
    - missing (list) of missing entitlements
  """

  if len(entitlements_required) is 0:
    print("ERROR: No entitlements provided.\
          example call: hasEntitlements(entitlements=['CanGetAnyUser'])")
    exit(-1)

  fail = True # Default to fail
 
  current_entitlements = getEntitlementsCurrentUser()

  missing = []

  for entitlement in entitlements_required:
    if entitlement not in [ entitlement['role_name'] for entitlement in current_entitlements ]:
      missing.append(entitlement)
      
  if len(missing) == 0:
    fail = False
  else:
    print("ERROR: Missing entitlements")

  return fail, missing
