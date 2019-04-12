import requests
import os
import json
from .init import get_config

OBP_AUTH_TOKEN = os.getenv('OBP_AUTH_TOKEN', False)
OBP_API_HOST = os.getenv('OBP_API_HOST', False)

def sandboxImport(src=None):
  
  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')

  try: 
    payload = json.loads(src.read())
  except json.decoder.JSONDecodeError:
    exit("JSONDecodeError. Could not parse input into json. Abort")

  url = OBP_API_HOST + '/obp/v3.1.0/sandbox/data-import'

  authorization = 'DirectLogin token="{}"'.format(OBP_AUTH_TOKEN)
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  return req

if __name__ == '__main__':
  print(sandboxImport(OBP_AUTH_TOKEN=OBP_AUTH_TOKEN, OBP_API_HOST=OBP_API_HOST))

