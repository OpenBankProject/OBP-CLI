from .makeRequests import makePostRequest
from .init import get_config
from .hasEntitlements import checkForEntitlements

def getCustomerIdByCustomerNumber(customer_number=None, bank_id=None):
  """
  Get customer id by customer number.

  Required roles: CanGetCustomer
  e.g. obp addrole --role-name CanCreateCardsForBank --bank-id gh.29.uk.x
  """

  # Validate entitlements
  requiredEntitlements = ['CanGetCustomer']
  checkForEntitlements(requiredEntitlements)

  payload = { "customer_number": customer_number }

  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/customers/customer-number'.format(bank_id=bank_id,
            customer_number=customer_number)
  makePostRequest(url, payload)