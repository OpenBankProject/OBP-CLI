import requests
import os
import json
from .init import get_config

def getUserId():

  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')

  url = OBP_API_HOST + '/obp/v3.1.0/users/current'

  authorization = 'DirectLogin token="{}"'.format(OBP_AUTH_TOKEN)
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.get(url, headers=headers)

  return req

if __name__ == '__main__':
  print("Your user id is:")
  print(getUserId())

