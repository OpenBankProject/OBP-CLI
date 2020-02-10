from .init import get_config
from .makeRequests import makePostRequest


def createProductAttribute(
        bank_id=None,
        product_code=None,
        name=None,
        _type=None,
        value=None
        ):

    if type not in ("STRING", "INTEGER", "DOUBLE", "DATE_WITH_DAY"):
        print('type has to be one of: "STRING", "INTEGER", "DOUBLE" or "DATE_WITH_DAY"')
        exit(-1)

    payload = {
        "name": name,  "type": _type,  "value": value}

    url = get_config('OBP_API_HOST') \
    + '/obp/v4.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}/attribute'.format(BANK_ID=bank_id, PRODUCT_CODE=product_code)

    return makePostRequest(url, payload)
