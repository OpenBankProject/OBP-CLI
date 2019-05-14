import requests
import os
import json
from .init import get_config


def deleteBranches(bank_id): 
  # Get all branches
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{}/branches'.format(bank_id)
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.get(url, headers=headers)
  resp = json.loads(req.text)
  if 'branches' not in resp:
    return req
  branches = json.loads(req.text)['branches']

  ## Delete all branches
  branch_ids = []
  for branch in branches:
    branch_ids.append(branch['id'])

  for branch_id in branch_ids:
      url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{}/branches/{}'.format(bank_id, branch_id)
      print(url)
      authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
      headers = {'Content-Type': 'application/json',
                'Authorization': authorization}
      req = requests.delete(url, headers=headers)
      print (req.text)
