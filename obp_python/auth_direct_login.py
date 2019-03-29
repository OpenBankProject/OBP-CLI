import requests
import os

CONSUMER_KEY = os.getenv('CONSUMER_KEY', False)
OBP_USERNAME = os.getenv('OBP_USERNAME', False)
PASSWORD = os.getenv('PASSWORD', False)
OBP_ENDPOINT = os.getenv('OBP_ENDPOINT', False)

def getAuthToken(OBP_USERNAME='', CONSUMER_KEY='', PASSWORD='', OBP_ENDPOINT=''):
  authorization = 'DirectLogin username="{}", password="{}", consumer_key="{}"'.format(OBP_USERNAME, PASSWORD, CONSUMER_KEY)

  headers={ 
        'Accept': 'application/json', 
        'Authorization': authorization
  }

  OBP_ENDPOINT = OBP_ENDPOINT + '/my/logins/direct'

  req = requests.post(OBP_ENDPOINT, headers=headers)

  if req.status_code == 201 or req.status_code == 200:
    print(req.text)
  else:
    print(req.text)


if __name__ == '__main__':
  CONSUMER_KEY = input("CONSUMER_KEY --> ")
  OBP_USERNAME = input("OBP_USERNAME --> ")
  PASSWORD = input("PASSWORD --> ")
  OBP_ENDPOINT = input("OBP_ENDPOINT --> ")
  getAuthToken(OBP_USERNAME=OBP_USERNAME, CONSUMER_KEY=CONSUMER_KEY, PASSWORD=PASSWORD, OBP_ENDPOINT=OBP_ENDPOINT)
  
