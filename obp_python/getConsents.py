from .init import get_config
from .makeRequests import makeGetRequest


def getConsents(bank_id=None):
  """Get consents of the current user.
  
  Requires entitlements: 
  To add entitlements with cli: `obp addrole --role-name=<role-name>`
  """

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/my/consents'.format(bank_id=bank_id)
  
  makeGetRequest(url)
