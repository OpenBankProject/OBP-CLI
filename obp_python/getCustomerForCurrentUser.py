import requests
from .init import get_config
from .hasEntitlements import checkForEntitlements
from .makeRequests import makeGetRequest


def getCustomerForCurrentUser():


    url = get_config('OBP_API_HOST') + '/obp/v4.0.0/users/current/customers'

    return makeGetRequest(url)
