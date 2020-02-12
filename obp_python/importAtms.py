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

def importAtms(spreadsheet=None, sheet_name=None):
  
  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')
  '''
  Loading location data from ods spreadsheet
  '''
  sheetdata = get_data(spreadsheet).popitem() #Pops first sheet
  atms = []

  def get_value(index=None, obj=None):
      try:
        return obj[index]
      except IndexError:
        return ''

  def compute_atm_id_hash(atm):
    ''' Compute a branch_id by sha256 hashing the concatenated values:
        - bank_id
        - name
        - Line_1
    '''
    # Concat values
    m = sha256()
    m.update(get_value(0, atm).encode("utf-8")) #bank_id
    m.update(get_value(1, atm).encode("utf-8")) #name
    m.update(get_value(2, atm).encode("utf-8")) #Line_1
    return  m.hexdigest()[0:43]

  for index, atm in enumerate(sheetdata[1:][0][1:]): #skips sheetname, and header
    try:
      if atm == []:
        continue; # Skip blank lines
      bank_id = get_value(0, atm)
      atm_id = compute_atm_id_hash(atm)
      name = get_value(1, atm)
      addr1 = get_value(2, atm)
      addr2 = get_value(3, atm)
      addr3 = get_value(4, atm)
      city = get_value(5, atm)
      county = get_value(6, atm)
      state = get_value(7, atm)
      label = get_value(0, atm)
      postcode = get_value(8, atm)
      county_code = get_value(9, atm)
      latitude = get_value(10, atm)
      if latitude is not '':
          latitude = float(latitude) 
      else:
          latitude = float('0')
      longitude = get_value(11, atm)
      if longitude is not '':
          longitude = float(longitude)
      else:
          longitude = float('0')
      located_at = get_value(12, atm)
      has_deposit_capability = get_value(13, atm)
      is_accessible = get_value(14, atm)
      more_info = get_value(15, atm)
      

      #Build atm object
      atm = {
        'id': str(atm_id),
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
            'latitude': latitude,
            'longitude': longitude
        },
        'meta': {
          'license': {
              'id': 'PDDL',
              'name': 'Open Data Commons Public Domain Dedication and License'
           }
        },
          'monday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
          'tuesday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
          'wednesday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
          'thursday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
          'friday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
          'saturday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
          'sunday': [{'opening_time': '09:00', 'closing_time': '16:00'}],
          'is_accessible': is_accessible,
          'located_at': located_at,
          'more_info' : more_info,
          'has_deposit_capability': has_deposit_capability
        }
      atms.append(atm)
    except Exception as e:
      traceback.print_exc(file=sys.stdout)

  #Post atms to api
  sucessCount = 0
  failCount = 0
  failedAtms = []
  for payload in atms:
      authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
      headers = {'Content-Type': 'application/json',
                'Authorization': authorization}
      url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{}/atms'.format(bank_id)
      response = requests.post(url, json=payload, headers=headers)

      print(response.text)
      if response.status_code is not 201:
        print(response.text)
        failCount = failCount + 1
        failedAtms.append(payload)
      elif response.status_code == 201:
        print(response.text)
        sucessCount = sucessCount + 1


  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
  print("The atms which failed to import, if any,  were:")
  for atm in failedAtms:
    print(atm)
  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
