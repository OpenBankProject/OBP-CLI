import requests
import os
import json
from .init import get_config
from dms2dec.dms_convert import dms2dec
from pyexcel_ods import get_data
from random import randint
import sys, traceback
import re
from hashlib import sha256

def importBranches(spreadsheet=None, sheet_name=None):
  
  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')
  '''
  Loading location data from ods spreadsheet
  '''
  sheetdata = get_data(spreadsheet).popitem() #Pops first sheet
  branches = []

  def get_value(index=None, obj=None):
      try:
        return obj[index]
      except IndexError:
        return ''

  def compute_branch_id_hash(branch):
    ''' Compute a branch_id by sha256 hashing the concatenated values:
        - bank_id
        - name
        - Line_1
    '''
    # Concat values
    m = sha256()
    m.update(get_value(0, branch).encode("utf-8")) #bank_id
    m.update(get_value(1, branch).encode("utf-8")) #name
    m.update(get_value(2, branch).encode("utf-8")) #Line_1
    return  m.hexdigest()

  for index, branch in enumerate(sheetdata[1:][0][1:]): #skips sheetname, and header
    try:
      if branch == []:
        continue; # Skip blank lines
      bank_id = get_value(0, branch)
      branch_id = compute_branch_id_hash(branch)
      name = get_value(1, branch)
      addr1 = get_value(2, branch)
      addr2 = get_value(3, branch)
      addr3 = get_value(4, branch)
      city = get_value(5, branch)
      county = get_value(6, branch)
      state = get_value(7, branch)
      label = get_value(0, branch)
      postcode = get_value(8, branch)
      county_code = get_value(9, branch)
      latitude = get_value(10, branch)
      longitude = get_value(11, branch)
      branch_routing_scheme = get_value(12, branch)
      is_accessible = get_value(14, branch)
      accessible_features = get_value(15, branch)
      branch_type = get_value(16, branch)
      phone_number = get_value(17, branch)
      more_info = get_value(18, branch)
      lobby_monday_opening_time = get_value(21, branch).strftime('%H:%M')

      #Build branch object
      branch = {
        'id': str(branch_id),
        'bank_id' : bank_id,
        'name': name,
        'address': {
            'line_1': addr1,
            'line_2': addr2,
            'line_3': addr3,
            'city': city,
            'state': state,
            'county': county,
            'postcode': str(postcode),
            'country_code': county_code
        },
        'location' : {
            'latitude': float(latitude),
            'longitude': float(longitude)
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
          'is_accessible': is_accessible,
          'accessibleFeatures': accessible_features,
          'branch_type': branch_type,
          'more_info' : more_info,
          'phone_number': phone_number
        }
      branches.append(branch)
    except Exception as e:
      traceback.print_exc(file=sys.stdout)

  #Post branches to api
  sucessCount = 0
  failCount = 0
  failedBranches = []
  for payload in branches:
      authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
      headers = {'Content-Type': 'application/json',
                'Authorization': authorization}
      url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{}/branches'.format(bank_id)
      response = requests.post(url, json=payload, headers=headers)

      print(response.text)
      if response.status_code is not 201:
        print(response.text)
        failCount = failCount + 1
        failedBranches.append(payload)
      elif response.status_code == 201:
        print(response.text)
        sucessCount = sucessCount + 1


  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
  print("The branches which failed to import, if any,  were:")
  for branch in failedBranches:
    print(branch)
  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
