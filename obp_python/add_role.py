import requests
import os

AUTH_TOKEN = os.getenv('AUTH_TOKEN', False)
OBP_API_HOST = os.getenv('OBP_API_HOST', False)
USER_ID = os.getenv('USER_ID', False)

def addRole(role=None):


  url = OBP_API_HOST + '/obp/v3.1.0/users/{}/'.format(USER_ID) + 'entitlements'

  payload = {"bank_id":"", "role_name": role}

  authorization = 'DirectLogin token="{}"'.format(AUTH_TOKEN)
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  request = requests.post(url, headers=headers, json=payload)

  print(request.text)

if __name__ == '__main__':
  role = input("Role wanted -->")
  addRole(role=role)

