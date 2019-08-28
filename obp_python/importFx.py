import requests
from .init import get_config
import sys, traceback
from .hasEntitlements import hasEntitlements
from fx2obp import postFx

def importFx(spreadsheet=None, sheet_name=None):
  """
  Import cards into Open Bank Project

  Required roles: CanCreateFxRate or CanCreateFxRateAtAnyBank
  e.g. obp addrole --role-name CanCreateFxRateAtAnyBank --bank-id gh.29.uk.x
  """

  # Validate entitlements
  requiredEntitlements = ['CanCreateFxRateAtAnyBank']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)
  
  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')

  postFx(ephemeral=True, POST_TO_OBP=True, WRITE_TO_FILE=False, AUTH_TOKEN=OBP_AUTH_TOKEN,
          API_HOST=OBP_API_HOST )

  return 1

