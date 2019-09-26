import requests
import os
import json
from .init import get_config
from .hasEntitlements import checkForEntitlements
from .makeRequests import makePutRequest

def addKycMedia(
        bank_id=None,
        customer_id=None,
        kyc_media_id=None,
        customer_nr=None,
        Type=None,
        input_url=None,
        date=None,
        kyc_document_id=None,
        kyc_check_id=None):

  checkForEntitlements(['CanAddKycMedia'])

  payload = {
      "customer_number": customer_nr,
      "type": Type,
      "url": input_url,
      "date": date,
      "relates_to_kyc_document_id": kyc_document_id,
      "relates_to_kyc_check_id": kyc_check_id}

  url = get_config('OBP_API_HOST') \
      + '/obp/v4.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_media/{KYC_MEDIA_ID}'.format(
      BANK_ID=bank_id,
      CUSTOMER_ID=customer_id,
      KYC_MEDIA_ID=kyc_media_id)

  return makePutRequest(url, payload)
