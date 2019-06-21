import requests
from .init import get_config
from pyexcel_ods import get_data
import sys, traceback
from .createCard import createCard
from .getCustomerIdByCustomerNumber import getCustomerIdByCustomerNumber
from .addCardAttribute import addCardAttribute
from .hasEntitlements import hasEntitlements

def importCardAttributes(spreadsheet=None, sheet_name=None):
  """
  Attatch card attributes to cards.

  Required roles: CanGetCardsForBank
  e.g. obp addrole --role-name [role-name] --bank-id gh.29.uk.x
  """

  # Validate entitlements
  requiredEntitlements = ['CanGetCardsForBank']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)
  
  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')

  sheetdata = get_data(spreadsheet).popitem() #Pops first sheet

  def get_value(index=None, obj=None):
      try:
        return obj[index]
      except IndexError:
        return ''
  sucessCount = 0
  failCount = 0
  failedAttributes = []

  for index, attribute in enumerate(sheetdata[1:][0][1:]): #skips sheetname, and header
    try:
      bank_id = get_value(0, attribute)
      card_number = get_value(1, attribute)
      name = get_value(2, attribute)
      attribute_type = get_value(3, attribute)
      value = get_value(4, attribute)

      #Post card attribute to api
      response = addCardAttribute(bank_id=bank_id, card_number=card_number,
                                  name=name, attribute_type=attribute_type,
                                  value=value)

      print(response.text)
      if response.status_code == 400:
        print("WARNING: card attribute aleady exists")
        print(response.text)
        sucessCount = sucessCount + 1
      elif response.status_code is 201:
        print(response.text)
        sucessCount = sucessCount + 1
      else:
        print(response.text)
        failCount = failCount + 1
        failedCards.append(attribute)
      
    except Exception as e:
      traceback.print_exc(file=sys.stdout)



  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
  print("The attributes which failed to import, if any,  were:")
  for attribute in failedAttributes:
    print(attribute)
  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
