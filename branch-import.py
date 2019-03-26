import requests
from dms_convert import dms2dec
from pyexcel_ods import get_data

## Example 
'''
Loading location data from ods spreadsheet, see sample
'''


## Read from sheet

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
    data = payload 
    headers = {'Authorization':'DirectLogin token="<>'}
    response = requests.post('https://bnpparibas-irb.openbankproject.com/obp/v3.0.0/banks/bnpp-irb.01.dz.dz/branches', json=data, headers=headers)
    print(response.text)

'''
## Delete all branches

branch_ids = []
for branch in branches:
  branch_ids.append(branch['id'])

for branch_id in branch_ids:
    placeholder = 'https://bnpparibas-irb.openbankproject.com/obp/v3.1.0/banks/bnpp-irb.01.dz.dz/branches/{}'
    url = placeholder.format(branch_id.encode('utf-8'))
    headers = {'Authorization':'DirectLogin token="<>"'}
    response = requests.delete(url, json=data, headers=headers)
    print response.text
''' 
