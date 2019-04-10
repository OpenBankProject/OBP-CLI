import requests
import os

OBP_AUTH_TOKEN = os.getenv('OBP_AUTH_TOKEN', False)
OBP_API_HOST = os.getenv('OBP_API_HOST', False)
USER_ID = os.getenv('USER_ID', False)
OBP_BANK_ID = os.getenv('OBP_BANK_ID', "")

def addRole(role=None):


  url = OBP_API_HOST + '/obp/v3.1.0/users/{}/'.format(USER_ID) + 'entitlements'

  payload = {"bank_id":OBP_BANK_ID, "role_name": role}

  authorization = 'DirectLogin token="{}"'.format(OBP_AUTH_TOKEN)
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  request = requests.post(url, headers=headers, json=payload)

  print(request.text)

if __name__ == '__main__':
  role = input("Role wanted -->")
  addRole(role=role)

