import requests
import os
import json
from .init import get_config
from .hasEntitlements import checkForEntitlements
from .makeRequests import makePutRequest

def addKycStatus(
        bank_id=None,
        customer_id=None,
        customer_nr=None,
        ok=None,
        date=None):

  checkForEntitlements(['CanAddKycStatus'])

  payload = {
      "customer_number": customer_nr,
      "ok": ok,
      "date": date}

  url = get_config('OBP_API_HOST') \
      + '/obp/v4.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_statuses'.format(
      BANK_ID=bank_id,
      CUSTOMER_ID=customer_id)

  return makePutRequest(url, payload)
