import requests
from dms_convert import dms2dec
from pyexcel_ods import get_data
from random import randint
import sys, traceback
import re

## Example 
'''
Loading location data from ods spreadsheet
'''

AUTH_TOKEN = os.getenv('AUTH_TOKEN', False)
OBP_IMPORT_SHEET_NAME = os.getenv("OBP_IMPORT_SHEET_NAME", False)
OBP_BANK_ID = os.getenv("OBP_BANK_ID", False)

def get_value(index=None, obj=None):
    try:
      return obj[index]
    except IndexError:
      return ''

## Read from sheet
sheetdata = get_data('geoloc-branches.ods')
branches = []
for index, branch in enumerate(sheetdata[OBP_IMPORT_SHEET_NAME][1:]):
  try:
    if branch == []:
      continue; # Skip blank lines
    branch_id = get_value(3, branch)
    name = get_value(8, branch)
    addr1 = get_value(4, branch)
    city = get_value(7, branch)
    label = get_value(8, branch)
    postcode = get_value(6, branch)
    latitude = dms2dec(branch[0])
    longitude = dms2dec(branch[1])
    if branch_id is '':
      branch_id = str(randint(100,1000)) + city + label
      branch_id = ascii(re.sub(r'\W+', '', branch_id)).replace('\\','')
      print("Try getting id: {}".format(branch_id))

    branch = {
      'id': str(branch_id),
      'bank_id' : 'bnpp-irb.01.dz.dz',
      'name': name,
      'address': {
          'line_1': addr1,
          'line_2': '',
          'line_3': '',
          'city': city,
          'state': '',
          'county': '',
          'postcode': str(postcode),
          'country_code': 'DZ'
      },
      'location' : {
          'latitude': latitude,
          'longitude': longitude
      },
      'meta': {
        'license': {
            'id': 'PDDL', 
            'name': 'Open Data Commons Public Domain Dedication and License'
         }
      },
      'lobby': {
        'monday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
        'tuesday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
        'wednesday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
        'thursday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
        'friday': [{'opening_time': '', 'closing_time': ''}],
        'saturday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
        'sunday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
      },
      'drive_up': {
        'monday': {'opening_time': '', 'closing_time': ''},
        'tuesday': {'opening_time': '', 'closing_time': ''},
        'wednesday': {'opening_time': '', 'closing_time': ''},
        'thursday': {'opening_time': '', 'closing_time': ''},
        'friday': {'opening_time': '', 'closing_time': ''},
        'saturday': {'opening_time': '', 'closing_time': ''},
        'sunday': {'opening_time': '', 'closing_time': ''},
      },
      'branch_routing': {
            'scheme': 'OBP',
            'address': '123abc'},
      'is_accessible': "false",
      'accessibleFeatures': '',
      'branch_type': '',
      'more_info' : '',
      'phone_number': branch[10]
    }
    branches.append(branch)
  except Exception as e:
    traceback.print_exc(file=sys.stdout) 
    pass

#Post to api endpoint
sucessCount = 0
failCount = 0
for payload in branches:
    headers = {'Authorization':'DirectLogin token=""'}
    authorization = 'DirectLogin token="{}"'.format(AUTH_TOKEN)
    headers = {'Content-Type': 'application/json',
               'Authorization': authorization}
    url = OBP_API_HOST + '/obp/v3.1.0/banks/{}/branches'.format(OBP_BANK_ID)
    response = requests.post(url, json=data, headers=headers)

    print(response.text)
    if response.status_code is not 201:
      failCount = failCount + 1
    elif response.status_code == 201:
      sucessCount = sucessCount + 1


print("Success: {}".format(sucessCount))
print("Failed: {}".format(failCount))
