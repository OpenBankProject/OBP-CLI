from .makeRequests import makeGetRequest
from .init import get_config

def revokeConsent(bank_id=None, consent_id=None):
  """Revoke a consent in Open Bank Project.
  
  Requires entitlements: 
  To add entitlements with cli: `obp addrole --role-name=<role-name>`
  """
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/my/consents/{consent_id}/revoke'.format(bank_id=bank_id, consent_id=consent_id)
  
  makeGetRequest(url)
