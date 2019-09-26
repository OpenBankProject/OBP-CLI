import requests
import os
import json
from .init import get_config
from .hasEntitlements import checkForEntitlements
from .makeRequests import makePutRequest

def addKycDocument(
        bank_id=None,
        customer_id=None,
        customer_nr=None,
        kyc_document_id=None,
        Type=None,
        number=None,
        issue_date=None,
        issue_place=None,
        expiry_date=None):

  checkForEntitlements(['CanAddKycDocument'])

  payload = {
    "customer_number": customer_nr,
    "type": Type,
    "number": number,
    "issue_date": issue_date,
    "issue_place": issue_place,
    "expiry_date": expiry_date
  }

  url = get_config('OBP_API_HOST') \
      + '/obp/v4.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_documents/{KYC_DOCUMENT_ID}'.format(
      BANK_ID=bank_id,
      CUSTOMER_ID=customer_id,
      KYC_DOCUMENT_ID=kyc_document_id)

  return makePutRequest(url, payload)
