import requests
import os
import json
from .init import get_config

def getUserIdByUsername(username=None):

  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')

  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/users/username/{username}'.format(username=username)
  req = requests.get(url, headers=headers)
  return req
