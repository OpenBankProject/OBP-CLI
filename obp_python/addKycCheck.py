import requests
import os
import json
from .init import get_config
from .hasEntitlements import checkForEntitlements
from .makeRequests import makePutRequest

def addKycCheck(
        bankid=None,
        customerid=None,
        customernr=None,
        kyccheckid=None,
        date=None,
        how=None,
        staff_user_id=None,
        staff_name=None,
        satisfied=None,
        comments=None):

  checkForEntitlements(['CanAddKycCheck'])

  payload = {
      "customer_number" : customernr,
      "date" : date,
      "how" : how,
      "staff_user_id" : staff_user_id,
      "staff_name" : staff_name,
      "satisfied" : satisfied,
      "comments" : comments}

  url = get_config('OBP_API_HOST') \
        + '/obp/v4.0.0/banks/{{BANK_ID}}/customers/{{CUSTOMER_ID}}/kyc_check/{{KYC_CHECK_ID}}'.format(
      BANK_ID=bankid,
      CUSTOMER_ID=customerid,
      KYC_CHECK_ID=kyccheckid)

  makePutRequest(url, payload)
