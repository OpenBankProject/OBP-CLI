import requests
from .init import get_config
from pyexcel_ods import get_data
import sys, traceback
from .createUser import createUser

def importUsers(spreadsheet=None, sheet_name=None):
  
  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')
  '''
  Loading location data from ods spreadsheet
  '''
  sheetdata = get_data(spreadsheet).popitem() #Pops first sheet
  users = []

  def get_value(index=None, obj=None):
      try:
        return obj[index]
      except IndexError:
        return ''
  sucessCount = 0
  failCount = 0
  failedUsers = []

  for index, user in enumerate(sheetdata[1:][0][1:]): #skips sheetname, and header
    try:
      username = get_value(0, user)
      email = get_value(1, user)
      password = get_value(2, user)
      first_name = get_value(3, user)
      last_name = get_value(4, user)

      #Post user to api
      response = createUser(username=username, email=email, 
                            password=password, 
                            first_name=first_name, 
                            last_name=last_name)

      print(response.text)
      if response.status_code is 200:
        print("WARNING: user aleady exists")
        print(response.text)
        sucessCount = sucessCount + 1
      elif response.status_code is 201:
        print(response.text)
        sucessCount = sucessCount + 1
      else:
        print(response.text)
        failCount = failCount + 1
        failedUsers.append(user)
      
    except Exception as e:
      traceback.print_exc(file=sys.stdout)



  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
  print("The users which failed to import, if any,  were:")
  for user in failedUsers:
    print(user)
  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
