from .init import get_config
from .hasEntitlements import checkForEntitlements
from .makeRequests import makeGetRequest


def getSocialMediaHandles(bank_id=None, customer_id=None):

    # Validate entitlements
    requiredEntitlements = ['CanGetSocialMediaHandles']
    checkForEntitlements(requiredEntitlements)
    url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/social_media_handles'.format(BANK_ID=bank_id, CUSTOMER_ID=customer_id)

    return makeGetRequest(url)
