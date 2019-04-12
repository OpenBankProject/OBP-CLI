import requests
import os
from .init import get_config

def addRole(role=None, require_bank_id=True):

  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')
  OBP_USER_ID = get_config('OBP_USER_ID')
  if require_bank_id:
    OBP_BANK_ID = get_config('OBP_BANK_ID')
  else:
    OBP_BANK_ID = ''

  url = OBP_API_HOST + '/obp/v3.1.0/users/{}/'.format(OBP_USER_ID) + 'entitlements'

  payload = {"bank_id":OBP_BANK_ID, "role_name": role}

  authorization = 'DirectLogin token="{}"'.format(OBP_AUTH_TOKEN)
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  return req

if __name__ == '__main__':
  role = input("Role wanted -->")
  addRole(role=role)

