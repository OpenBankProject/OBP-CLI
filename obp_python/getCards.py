import requests
from .init import get_config
from .hasEntitlements import hasEntitlements
from .makeRequests import makeGetRequest


def getCards(bank_id=None):

  # Validate entitlements
  requiredEntitlements = ['CanGetCardsForBank']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/management/banks/{bank_id}/cards'.format(bank_id=bank_id)
  
  makeGetRequest(url)
