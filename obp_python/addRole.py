import requests
import os
from .init import get_config

def addRole(role=None, bank_id=None):
  """
  Add a role/entitlement for the current user

  For options see `obp addrole --help`
  """

  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')
  OBP_USER_ID = get_config('OBP_USER_ID')
  if bank_id is None:
    payload = {"bank_id":"", "role_name": role}
  elif bank_id is not None:
    payload = {"bank_id": bank_id, "role_name": role}
  
  url = OBP_API_HOST + '/obp/v3.1.0/users/{}/'.format(OBP_USER_ID) + 'entitlements'

  authorization = 'DirectLogin token="{}"'.format(OBP_AUTH_TOKEN)
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  return req

if __name__ == '__main__':
  role = input("Role wanted -->")
  addRole(role=role)

