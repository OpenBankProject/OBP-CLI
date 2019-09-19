import requests
from .init import get_config
from pyexcel_ods import get_data
import sys, traceback
from .createCard import createCard
from .getCustomerIdByCustomerNumber import getCustomerIdByCustomerNumber
from .hasEntitlements import hasEntitlements

def importCards(spreadsheet=None, sheet_name=None):
  """
  Import cards into Open Bank Project

  Required roles: CanCreateCardsForBank, CanGetCustomer
  e.g. obp addrole --role-name CanCreateCardsForBank --bank-id gh.29.uk.x
  """

  # Validate entitlements
  requiredEntitlements = ['CanCreateCardsForBank', 'CanGetCustomer']
  fail, msg = hasEntitlements(entitlements_required=requiredEntitlements)

  if fail is True:
    print(msg)
    exit(-1)
  
  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')

  sheetdata = get_data(spreadsheet).popitem() #Pops first sheet
  cards = []

  def get_value(index=None, obj=None):
      try:
        return obj[index]
      except IndexError:
        return ''
  sucessCount = 0
  failCount = 0
  failedCards = []

  for index, card in enumerate(sheetdata[1:][0][1:]): #skips sheetname, and header
    try:
      bank_id = get_value(0, card)
      card_number = get_value(1, card)
      card_type = get_value(2, card)
      name_on_card = get_value(3, card)
      issue_number = get_value(4, card)
      serial_number = get_value(5, card)
      valid_from_date = get_value(6, card)
      expires_date = get_value(7, card)
      enabled = get_value(8, card)
      technology = get_value(9, card)
      networks = get_value(10, card)
      allows = get_value(11, card)
      account_id = get_value(12, card)
      replacement_requested_date = get_value(13, card)
      replacement_reason_requested = get_value(14, card)
      pin_reset_requested_date = get_value(15, card)
      pin_reset_reason_requested = get_value(16, card)
      collected = get_value(17, card)
      posted = get_value(18, card)
      customer_number = get_value(19, card)

      # Work out customer id
      req = getCustomerIdByCustomerNumber(bank_id=bank_id,
                    customer_number=customer_number)
      if req.status_code == 200 or req.status_code == 201:
        customer_id = req.json()['customer_id']
      else:
        print("ERROR: Could not determin customer_id")
        print(req)
        exit(-1)

      #Post card to api
      response = createCard(bank_id=bank_id, card_number=card_number,
                  card_type=card_type, name_on_card=name_on_card, issue_number=issue_number,
                  serial_number=serial_number, valid_from_date=valid_from_date, 
                  expires_date=expires_date, enabled=enabled, 
                  technology=technology, networks=networks, allows=allows,
                  account_id=account_id, 
                  replacement_requested_date=replacement_requested_date,
                  replacement_reason_requested=replacement_reason_requested,
                  pin_reset_requested_date=pin_reset_requested_date,
                  pin_reset_reason_requested=pin_reset_reason_requested, 
                  collected=collected, posted=posted,
                  customer_id=customer_id)

      print(response.text)
      if response.status_code == 400 and "Card already exists" in response.text:
        print("WARNING: card aleady exists")
        print(response.text)
        sucessCount = sucessCount + 1
      elif response.status_code is 201:
        print(response.text)
        sucessCount = sucessCount + 1
      else:
        print(response.text)
        failCount = failCount + 1
        failedCards.append(card)
      
    except Exception as e:
      traceback.print_exc(file=sys.stdout)



  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
  print("The cards which failed to import, if any,  were:")
  for card in failedCards:
    print(card)
  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
