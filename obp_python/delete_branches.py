import requests
import json
import os

OBP_API_HOST = os.getenv('OBP_API_HOST', False)
OBP_BANK_ID = os.getenv('OBP_BANK_ID', False)
OBP_AUTH_TOKEN = os.getenv('OBP_AUTH_TOKEN', False)

# Get all branches
url = "{}/obp/v3.1.0/banks/{}/branches".format(OBP_API_HOST, OBP_BANK_ID)
headers = {'Authorization':'DirectLogin token="{}"'.format(OBP_AUTH_TOKEN)}
response = requests.get(url, headers=headers)
branches = json.loads(response.text)['branches']

## Delete all branches
branch_ids = []
for branch in branches:
  branch_ids.append(branch['id'])

for branch_id in branch_ids:
    url = "{}/obp/v3.1.0/banks/{}/branches/{}".format(OBP_API_HOST, OBP_BANK_ID, branch_id)
    print(url)
    headers = {'Authorization':'DirectLogin token="{}"'.format(OBP_AUTH_TOKEN)}
    response = requests.delete(url, headers=headers)
    print (response.text)
