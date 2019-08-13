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
    allowed_actions=[],  # Comma seperated list of allowed actions.
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
        "allowed_actions": allowed_actions.split(","),
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


possible_actions = """can_see_transaction_this_bank_account,can_see_transaction_other_bank_account,can_see_transaction_metadata,can_see_transaction_label,can_see_transaction_amount,can_see_transaction_type,can_see_transaction_currency,can_see_transaction_start_date,can_see_transaction_finish_date,can_see_transaction_balance,can_see_comments,can_see_narrative,can_see_tags,can_see_images,can_see_bank_account_owners,can_see_bank_account_type,can_see_bank_account_balance,can_see_bank_account_currency,can_see_bank_account_label,can_see_bank_account_national_identifier,can_see_bank_account_swift_bic,can_see_bank_account_iban,can_see_bank_account_number,can_see_bank_account_bank_name,can_see_other_account_national_identifier,can_see_other_account_swift_bic,can_see_other_account_iban,can_see_other_account_bank_name,can_see_other_account_number,can_see_other_account_metadata,can_see_other_account_kind,can_see_more_info,can_see_url,can_see_image_url,can_see_open_corporates_url,can_see_corporate_location,can_see_physical_location,can_see_public_alias,can_see_private_alias,can_add_more_info,can_add_url,can_add_image_url,can_add_open_corporates_url,can_add_corporate_location,can_add_physical_location,can_add_public_alias,can_add_private_alias,can_delete_corporate_location,can_delete_physical_location,can_edit_narrative,can_add_comment,can_delete_comment,can_add_tag,can_delete_tag,can_add_image,can_delete_image,can_add_where_tag,can_see_where_tag,can_delete_where_tag,can_create_counterparty,can_see_bank_routing_scheme,can_see_bank_routing_address,can_see_bank_account_routing_scheme,can_see_bank_account_routing_address,can_see_other_bank_routing_scheme,can_see_other_bank_routing_address,can_see_other_account_routing_scheme,can_see_other_account_routing_address,can_query_available_funds"""
