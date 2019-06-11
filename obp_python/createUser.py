import requests
import os
import json
from .init import get_config

def createUser(username=None, email=None, password=None, 
                first_name=None, last_name=None):

  payload = {
      "username": username,
      "email": email,
      "password": password,
      "first_name": first_name,
      "last_name": last_name
    }
  
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/users'
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  return req
