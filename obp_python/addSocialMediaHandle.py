import requests
import os
import json
from .init import get_config
from .hasEntitlements import checkForEntitlements
from .makeRequests import makePostRequest

def addSocialMediaHandle(
        bank_id=None,
        customer_id=None,
        customer_nr=None,
        type=None,
        handle=None,
        date_added=None,
        date_activated=None):

  checkForEntitlements(['CanAddSocialMediaHandle'])

  payload = {
      "customer_number": customer_nr,
      "type": type,
      "handle": handle,
      "date_added": date_added,
      "date_activated":date_activated}

  url = get_config('OBP_API_HOST') \
      + '/obp/v4.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/social_media_handles'.format(
      BANK_ID=bank_id,
      CUSTOMER_ID=customer_id,
      )

  return makePostRequest(url, payload)
