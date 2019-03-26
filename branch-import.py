import urllib2
from bs4 import BeautifulSoup
import json
import re 
import requests
from dms_convert import dms2dec


'''
# Strip from a website using beautiful soup; example using google maps
#fp = open('soup.txt') //useful for offline testing
#doc = fp.read()
response = urllib2.urlopen('https://www.bnpparibas.dz/trouver-une-agence/')
doc = response.read()

soup = BeautifulSoup(doc, 'html.parser')

branches = []

for elm in soup.find_all("li", class_="agency-orange"):
    cityAndPostcode = elm.find_all('a', class_='button3')[0].parent.next_sibling.next_sibling.next_element.next_element.next_element.replace('\n\t\t\t\t\t\t', '')
    cityAndPostcode = re.split("([0-9]+)", cityAndPostcode)

    city = cityAndPostcode[2].strip()
    postcode = cityAndPostcode[1].strip()
    name = elm.find_all('a', class_='button3')[0].text

    branch_id = ''.join([name, '-', postcode]).replace(' ','').lower()

    branch = {
      'id': branch_id,
      'bank_id' : 'bnpp-irb.01.dz.dz',
      'name': name,
      'address': {
          'line_1': elm.find_all('a', class_='button3')[0].parent.next_sibling.next_sibling.next_element.strip(),
          'line_2': '',
          'line_3': '',
          'city': city,
          'state': '',
          'county': '',
          'postcode': postcode,
          'country_code': 'DZ'
      },
      'location' : {
          'latitude': 10.0,
          'longitude': 10.0
      },
      'meta': {
        'license': {
            'id': 'PDDL', 
            'name': 'Open Data Commons Public Domain Dedication and License'
         }
      },
      'lobby': {
        'monday': [{'opening_time': '', 'closing_time': ''}],
        'tuesday': [{'opening_time': '', 'closing_time': ''}],
        'wednesday': [{'opening_time': '', 'closing_time': ''}],
        'thursday': [{'opening_time': '', 'closing_time': ''}],
        'friday': [{'opening_time': '', 'closing_time': ''}],
        'saturday': [{'opening_time': '', 'closing_time': ''}],
        'sunday': [{'opening_time': '', 'closing_time': ''}],
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
      'phone_number': ''
    }
    branches.append(branch)
    #import pdb;pdb.set_trace()

# Post to api endpoint
for payload in branches[2:-1]:
    data = payload #json.dumps(branches[0])
    headers = {'Authorization':'DirectLogin token="eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.zQnItv_eTUrD38DHD2oC5Hset_qKx8ixODQ2Q8UGM9A'}
    #response = requests.post('https://bnpparibas-irb.openbankproject.com/obp/v3.0.0/banks/bnpp-irb.01.dz.dz/branches', json=data, headers=headers)
'''

'''
## Delete all branches

branch_ids = []
for branch in branches:
  branch_ids.append(branch['id'])

for branch_id in branch_ids:
    placeholder = 'https://bnpparibas-irb.openbankproject.com/obp/v3.1.0/banks/bnpp-irb.01.dz.dz/branches/{}'
    url = placeholder.format(branch_id.encode('utf-8'))
    headers = {'Authorization':'DirectLogin token="eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.cqgmF73QHelglme8Rjlcv-fXRiyG9DO7d1Ggfw1kOWM"'}
    response = requests.delete(url, json=data, headers=headers)
    print response.text
''' 

## Read from sheet
from pyexcel_ods import get_data

sheetdata = get_data('geoloc-branches.ods')
branches = []
for branch in sheetdata['algeriev2_branch_data_critinfo_'][1:-1]:
  try:
    branch_id = str(branch[3])
    name = branch[8]
    addr1 = branch[4]
    city = branch[7]
    postcode = str(branch[6])
    latitude = dms2dec(branch[0])
    longitude = dms2dec(branch[1])

    branch = {
      'id': branch_id,
      'bank_id' : 'bnpp-irb.01.dz.dz',
      'name': name,
      'address': {
          'line_1': addr1,
          'line_2': '',
          'line_3': '',
          'city': city,
          'state': '',
          'county': '',
          'postcode': postcode,
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
        'monday': [{'opening_time': '', 'closing_time': ''}],
        'tuesday': [{'opening_time': '', 'closing_time': ''}],
        'wednesday': [{'opening_time': '', 'closing_time': ''}],
        'thursday': [{'opening_time': '', 'closing_time': ''}],
        'friday': [{'opening_time': '', 'closing_time': ''}],
        'saturday': [{'opening_time': '', 'closing_time': ''}],
        'sunday': [{'opening_time': '', 'closing_time': ''}],
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
      'phone_number': ''
    }
    branches.append(branch)
  except Exception:
    pass

#Post to api endpoint
for payload in branches:
    data = payload #json.dumps(branches[0])
    headers = {'Authorization':'DirectLogin token="eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.gtmGS_vSMIJ_x668hjip45TItcsZ57zIfC_lhAfGn-s'}
    response = requests.post('https://bnpparibas-irb.openbankproject.com/obp/v3.0.0/banks/bnpp-irb.01.dz.dz/branches', json=data, headers=headers)
    print(response.text)

