import requests
from .init import get_config
from .getEntitlementsCurrentUser import getEntitlementsCurrentUser

def hasEntitlements(entitlements_required=[]):
  """
  Check current user has entitlements
  
  Returns: 
    - fail (bolean)
    - missing (list) of missing entitlements

  TODO Check if bank_id required
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
    print("To add an entitlement try:")
    print("obp addrole --role-name {role}".format(role=missing[0]))
    print("Alternatively...")
    print("obp addrole --role-name {role} --bank-id your-bank-id".format(role=missing[0]))

  return fail, missing
