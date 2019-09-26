import requests
from .init import get_config
from .hasEntitlements import hasEntitlements
from .makeRequests import makeGetRequest


def getCustomerKycDocuments(customer_id=None):

    # Validate entitlements
    requiredEntitlements = ['CanGetKycDocuments']
    fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

    if fail is True:
      print(msg)
      exit(-1)
    url = get_config('OBP_API_HOST') + '/obp/v4.0.0/customers/{customer_id}/kyc_documents'.format(customer_id=customer_id)

    return makeGetRequest(url)
