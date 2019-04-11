import requests
import os
import json
from .init import get_config

def getAuthToken(OBP_USERNAME=None, OBP_CONSUMER_KEY=None, OBP_PASSWORD=None, OBP_API_HOST=None):

  if OBP_CONSUMER_KEY is None:
    OBP_CONSUMER_KEY = get_config("OBP_CONSUMER_KEY")
  if OBP_USERNAME is None:
    OBP_USERNAME = get_config("OBP_USERNAME")
  if OBP_PASSWORD is None:
    OBP_PASSWORD = get_config("OBP_PASSWORD")
  if OBP_API_HOST is None:
    OBP_API_HOST = get_config("OBP_API_HOST")

  authorization = 'DirectLogin username="{}", password="{}", consumer_key="{}"'.format(OBP_USERNAME, OBP_PASSWORD, OBP_CONSUMER_KEY)

  headers={ 
        'Accept': 'application/json', 
        'Authorization': authorization
  }

  OBP_API_HOST = OBP_API_HOST + '/my/logins/direct'

  req = requests.post(OBP_API_HOST, headers=headers)

  return req


if __name__ == '__main__':
  OBP_CONSUMER_KEY = input("OBP_CONSUMER_KEY --> ")
  OBP_USERNAME = input("OBP_USERNAME --> ")
  OBP_PASSWORD = input("OBP_PASSWORD --> ")
  OBP_API_HOST = input("OBP_API_HOST --> ")
  print("Your auth token is:")
  print(getAuthToken(OBP_USERNAME=OBP_USERNAME, OBP_CONSUMER_KEY=OBP_CONSUMER_KEY, OBP_PASSWORD=OBP_PASSWORD, OBP_API_HOST=OBP_API_HOST))
  
