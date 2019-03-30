import requests
import os
import json

OBP_AUTH_TOKEN = os.getenv('AUTH_TOKEN', False)
OBP_ENDPOINT = os.getenv('OBP_ENDPOINT', False)

def getUserId(OBP_AUTH_TOKEN=OBP_AUTH_TOKEN, OBP_ENDPOINT=OBP_ENDPOINT):


  url = OBP_ENDPOINT + '/obp/v3.1.0/users/current'

  authorization = 'DirectLogin token="{}"'.format(OBP_AUTH_TOKEN)
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.get(url, headers=headers)

  if req.status_code == 201 or req.status_code == 200:
    return json.loads(req.text)['user_id']
  else:
    return json.loads(req.text)

  print(req.text)
  return json.loads(req.text)

if __name__ == '__main__':
  OBP_AUTH_TOKEN = input("OBP_AUTH_TOKEN -->")
  OBP_ENDPOINT = input("OBP_ENDPOINT -->")
  print("Your user id is:")
  print(getUserId(OBP_AUTH_TOKEN=OBP_AUTH_TOKEN, OBP_ENDPOINT=OBP_ENDPOINT))

