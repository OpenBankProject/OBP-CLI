import requests
import os
import json
from .init import get_config
from .hasEntitlements import checkForEntitlements
from .makeRequests import makePutRequest

def addKycCheck(
        bank_id=None,
        customer_id=None,
        customer_nr=None,
        kyc_check_id=None,
        date=None,
        how=None,
        staff_user_id=None,
        staff_name=None,
        satisfied=None,
        comments=None):

  checkForEntitlements(['CanAddKycCheck'])

  payload = {
      "customer_number" : customer_nr,
      "date" : date,
      "how" : how,
      "staff_user_id" : staff_user_id,
      "staff_name" : staff_name,
      "satisfied" : satisfied,
      "comments" : comments}

  url = get_config('OBP_API_HOST') \
        + '/obp/v4.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_check/{KYC_CHECK_ID}'.format(
      BANK_ID=bank_id,
      CUSTOMER_ID=customer_id,
      KYC_CHECK_ID=kyc_check_id)

  makePutRequest(url, payload)
