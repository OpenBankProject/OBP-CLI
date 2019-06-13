import requests
from .init import get_config
from pyexcel_ods import get_data
import sys, traceback
from .createCustomer import createCustomer
from .getUserIdByUsername import getUserIdByUsername
from .linkUserToCustomer import linkUserToCustomer
from .updateCustomerNumber import updateCustomerNumber


def importCustomers(spreadsheet=None, sheet_name=None):
  
  OBP_AUTH_TOKEN = get_config('OBP_AUTH_TOKEN')
  OBP_API_HOST = get_config('OBP_API_HOST')
  '''
  Loading location data from ods spreadsheet
  '''
  sheetdata = get_data(spreadsheet).popitem() #Pops first sheet
  customers = []

  def get_value(index=None, obj=None):
      try:
        return obj[index]
      except IndexError:
        return ''
  sucessCount = 0
  failCount = 0
  failedCustomers = []

  for index, customer in enumerate(sheetdata[1:][0][1:]): #skips sheetname, and header
    try:
      username = get_value(0, customer)
      bank_id = get_value(1, customer)
      customer_number = get_value(2, customer)
      legal_name = get_value(3, customer)
      mobile_phone_number = get_value(4, customer)
      email = get_value(5, customer)
      face_image_url = get_value(6, customer)
      face_image_date = get_value(7, customer)
      date_of_birth = get_value(8, customer)
      relationship_status = get_value(9, customer)
      dependants = get_value(10, customer)
      dob_of_dependants = get_value(11, customer)
      credit_rating_rating = get_value(12, customer)
      credit_rating_source = get_value(13, customer)
      credit_limit_currency = get_value(14, customer)
      credit_limit_amount= get_value(15, customer)
      highest_education_attained = get_value(16, customer)
      employment_status = get_value(17, customer)
      kyc_status = get_value(18, customer)
      last_ok_date = get_value(19, customer)
      title = get_value(20, customer)
      branch_id = get_value(21, customer)
      name_suffix = get_value(22, customer)

      #Post customer to api
      response = createCustomer(bank_id=bank_id, customer_number=customer_number, 
                                legal_name=legal_name, 
                                mobile_phone_number=mobile_phone_number,
                                email=email, face_image_url=face_image_date,
                                face_image_date=face_image_date, 
                                date_of_birth=date_of_birth,
                                relationship_status=relationship_status, 
                                dependants=dependants,
                                credit_rating_rating=credit_rating_rating, 
                                credit_rating_source=credit_rating_source, 
                                credit_limit_currency=credit_limit_currency, 
                                credit_limit_amount=credit_limit_amount,
                                highest_education_attained=highest_education_attained, 
                                employment_status=employment_status,
                                kyc_status=kyc_status, last_ok_date=last_ok_date, 
                                title=title, branch_id=branch_id, name_suffix=name_suffix)

      print(response.text)
      # Update customer number to the number specified in the spreadsheet
      # We need this because the createCustomer api call does not store the
      # customer number upon initial creation TODO change this.
      if response.status_code is 201 or response.status_code is 200:
        customer_id = response.json()['customer_id']
        updateCustomerNumber(bank_id=bank_id, customer_id=customer_id, 
                              customer_number=customer_number)
  
      # Link customer to 'username' if username is presnt in sheet
      if response.status_code is 201 or response.status_code is 200 \
        and bool(username) is not False:
        customer_id = response.json()['customer_id']
        req = getUserIdByUsername(username=username)
        if req.status_code is 200:
          user_id = req.json()['user_id']
          req = linkUserToCustomer(bank_id=bank_id, user_id=user_id,
                                    customer_id=customer_id)
          if req.status_code is not 201:
            print("WARNING: could not create link between User and Customer")

      if response.status_code is 200:
        print("WARNING: customer aleady exists")
        print(response.text)
        sucessCount = sucessCount + 1
      elif response.status_code is 201:
        print(response.text)
        sucessCount = sucessCount + 1
      else:
        print(response.text)
        failCount = failCount + 1
        failedCustomers.append(customer)
      
    except Exception as e:
      traceback.print_exc(file=sys.stdout)



  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
  print("The customers which failed to import, if any,  were:")
  for customer in failedCustomers:
    print(customer)
  print("Success: {}".format(sucessCount))
  print("Failed: {}".format(failCount))
