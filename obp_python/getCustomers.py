import requests
from .init import get_config
from .hasEntitlements import hasEntitlements

def getCustomers(bank_id=None):

  # Validate entitlements
  requiredEntitlements = ['CanUseFirehoseAtAnyBank']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/firehose/customers'.format(bank_id=bank_id)
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.get(url, headers=headers)
  
  if req.status_code == 403:
    if 'allow_firehose_views' in req.text:
      print(req.text)
      exit(-1) 

  return req
