import requests
from .makeRequests import makeGetRequest
from .init import get_config
from .hasEntitlements import hasEntitlements

def getCardById(bank_id=None, card_id=None):
  """
  Get card id by card number.

  Required roles: CanGetCardsForBank
  e.g. obp addrole --role-name --bank-id gh.29.uk.x
  """

  # Validate entitlements
  requiredEntitlements = ['CanGetCardsForBank']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)

  # First get all cards at bank (Open Bank Project does not provoide a get
  # card id by card number api call yet
  # https://github.com/OpenBankProject/OBP-API/issues/1328

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/management/banks/{bank_id}/cards/{card_id}'.format(bank_id=bank_id, card_id=card_id)
  return makeGetRequest(url)


  
