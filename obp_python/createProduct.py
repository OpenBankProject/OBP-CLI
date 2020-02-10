import requests
import os
import json
from .init import get_config
from .hasEntitlements import checkForEntitlements
from .makeRequests import makePutRequest


def createProduct(
        bank_id=None,
        product_code=None,
        name=None,
        parent_product_code=" ",
        category=None,
        family=None,
        superfamily=None,
        more_info_url=None,
        details=None,
        description=None,
        license_id=None,
        license_name=None
        ):

    payload = {"bank_id": bank_id,
             "name": name,
             "parent_product_code": parent_product_code,
             "category": category,
             "family": family,
             "super_family": superfamily,
             "more_info_url": more_info_url,
             "details": details,
             "description": description,  "meta": {"license": {"id": license_id, "name": license_name}}}

    url = get_config('OBP_API_HOST') \
    + '/obp/v4.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}'.format(BANK_ID=bank_id,PRODUCT_CODE=product_code)

    print(url)

    return makePutRequest(url, payload)
