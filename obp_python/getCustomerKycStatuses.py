from .init import get_config
from .hasEntitlements import checkForEntitlements
from .makeRequests import makeGetRequest


def getCustomerKYCstatuses(customer_id=None):

    # Validate entitlements
    requiredEntitlements = ['CanGetKycStatuses']
    checkForEntitlements(requiredEntitlements)
    url = get_config('OBP_API_HOST') + '/obp/v4.0.0/customers/{customer_id}/kyc_statuses'.format(customer_id=customer_id)

    return makeGetRequest(url)
