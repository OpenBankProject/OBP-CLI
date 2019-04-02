import requests
import os
import json

CONSUMER_KEY = os.getenv('CONSUMER_KEY', False)
OBP_USERNAME = os.getenv('OBP_USERNAME', False)
PASSWORD = os.getenv('PASSWORD', False)
OBP_API_HOST = os.getenv('OBP_API_HOST', False)
def getAuthToken(OBP_USERNAME=OBP_USERNAME, CONSUMER_KEY=CONSUMER_KEY, PASSWORD=PASSWORD, OBP_API_HOST=OBP_API_HOST):

  if CONSUMER_KEY is False:
    CONSUMER_KEY = input("CONSUMER_KEY --> ")
    OBP_USERNAME = input("OBP_USERNAME --> ")
    PASSWORD = input("PASSWORD --> ")
    OBP_API_HOST = input("OBP_API_HOST (include http:// or https://) --> ")
  authorization = 'DirectLogin username="{}", password="{}", consumer_key="{}"'.format(OBP_USERNAME, PASSWORD, CONSUMER_KEY)

  headers={ 
        'Accept': 'application/json', 
        'Authorization': authorization
  }

  OBP_API_HOST = OBP_API_HOST + '/my/logins/direct'

  req = requests.post(OBP_API_HOST, headers=headers)

  if req.status_code == 201 or req.status_code == 200:
    return json.loads(req.text)['token']
  else:
    return json.loads(req.text)


if __name__ == '__main__':
  CONSUMER_KEY = input("CONSUMER_KEY --> ")
  OBP_USERNAME = input("OBP_USERNAME --> ")
  PASSWORD = input("PASSWORD --> ")
  OBP_API_HOST = input("OBP_API_HOST --> ")
  print("Your auth token is:")
  print(getAuthToken(OBP_USERNAME=OBP_USERNAME, CONSUMER_KEY=CONSUMER_KEY, PASSWORD=PASSWORD, OBP_API_HOST=OBP_API_HOST))
  
