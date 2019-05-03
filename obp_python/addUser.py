import requests
import os
import json
from .init import get_config

OBP_API_HOST = os.getenv('OBP_API_HOST')

def addUser(email=None, username=None, password=None, firstname=None, 
            lastname=None):

  payload = {
        "email": email,
        "username": username,
        "password": password,
        "first_name": firstname,
        "last_name": lastname
  }
  
  url = get_config('OBP_API_HOST') + "/obp/v3.1.0/users"
  
  headers = {'Content-Type': 'application/json'}
  req = requests.post(url, headers=headers, json=payload)

  return req
