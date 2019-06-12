import requests
import os
import json
from .init import get_config

def createCustomer(username=None, bank_id=None, customer_number=None, 
                  legal_name=None, mobile_phone_number=None, email=None, 
                  face_image_url=None, face_image_date=None, date_of_birth=None, 
                  relationship_status=None, dependants=None, 
                  dob_of_dependants=None, credit_rating_rating=None, 
                  credit_rating_source=None, credit_limit_currency=None, 
                  credit_limit_amount=None, highest_education_attained=None, 
                  employment_status=None, kyc_status=None, 
                  last_ok_date=None, title=None, branch_id=None, 
                  name_suffix=None):
  """Create a customer in Open Bank Project.
  
  Requires entitlements: CanCreateCustomer or CanCreateCustomerAtAnyBank
  To add entitlements with cli: `obp addrole --role-name=<role-name>`
  """

  payload = {
            "legal_name": legal_name,
            "mobile_phone_number": mobile_phone_number,
            "email": email,  
            "face_image": { 
              "url": face_image_url,    
              "date": face_image_date  
            },
            "date_of_birth": date_of_birth, 
            "relationship_status": relationship_status,
            "dependants": dependants,
            "dob_of_dependants": ["2017-09-19T00:00:00Z"], #TODO Implement list parsing
            "credit_rating": {
                "rating": credit_rating_rating,
                "source": credit_rating_source
            },  
            "credit_limit": {    
                "currency": credit_limit_currency,    
                "amount": credit_limit_amount  
            },  
            "highest_education_attained": highest_education_attained,
            "employment_status": employment_status, 
            "kyc_status": kyc_status,
            "last_ok_date": last_ok_date,
            "title": title,
            "branchId": branch_id,
            "nameSuffix": name_suffix
  }
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/customers'.format(bank_id=bank_id)
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  return req
