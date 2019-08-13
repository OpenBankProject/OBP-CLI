import requests
import os
import json
from .init import get_config


def createView(
    bank_id=None,
    account_id=None,
    name=None,
    description=None,
    metadata_view=None,
    is_public=False,
    which_alias_to_use=None,
    hide_metadata_if_alias_used=False,
    allowed_actions=[],
):
    """
  Create a view in Open Bank Project

  Requires role: ...
  e.g. obp addrole --role-name <role-name>
  """

    payload = {
        "name": name,
        "description": description,
        "metadata_view": metadata_view,
        "is_public": True,
        "which_alias_to_use": which_alias_to_use,
        "hide_metadata_if_alias_used": hide_metadata_if_alias_used,
        "allowed_actions": allowed_actions,
    }

    url = get_config(
        "OBP_API_HOST"
    ) + "/obp/v3.1.0/banks/{bank_id}/accounts/{account_id}/views".format(
        bank_id=bank_id, account_id=account_id
    )

    authorization = 'DirectLogin token="{}"'.format(get_config("OBP_AUTH_TOKEN"))
    headers = {"Content-Type": "application/json", "Authorization": authorization}
    req = requests.post(url, headers=headers, json=payload)

    if req.status_code == 403:
        print(req.text)
        exit(-1)

    return req
