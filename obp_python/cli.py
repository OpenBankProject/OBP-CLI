import click
import json
import os
import sys
from .auth_direct_login import getAuthToken
from .init import (init_config_dir, set_obp_api_host, set_obp_username, 
                  set_obp_password, set_obp_consumer_key, set_obp_auth_token,
                  set_obp_user_id, get_config)
from .sandboxImport import sandboxImport
from .importBranches import importBranches
from .importAccounts import importAccounts
from .importTransactions import importTransactions
from .importUsers import importUsers
from .importCustomers import importCustomers
from .getUserId import getUserId
from .addRole import addRole
from .getUserId import getUserId
from .addUser import addUser
from .addFx import addFx
from .createAccount import createAccount
from .getBanks import getBanks
from .getAccountsHeld import getAccountsHeld
from .getAccount import getAccountById
from .deleteBranches import deleteBranches
from .getUserIdByUsername import getUserIdByUsername
import pprint

@click.group()
def cli():
  pass

@cli.command(help="🚜 Bulk import sandbox data from json input")
@click.option('--input', type=click.File('rb'), required=False, help="Import from file")
@click.option('--example', required=False, is_flag=True, 
              help="Auto import very small example dataset")
def sandboximport(input=None, example=False):
  if input is None and example is False:
    click.echo("Invalid option. See obp sandboximport --help", err=True)
    exit(-1)
  if example: #load example import 
    input = open(os.path.join(sys.prefix, 'obp_python/sandbox/example_import.json'))
  req = sandboxImport(src=input)
  if example:
    input.close()
  if req.status_code == 201 or req.status_code == 200:
    click.echo("Sandbox import complete")
  else:
    exit(req.text)


@cli.command(help="💡 Initalize connection to your Open Bank Project instance")
def init():
  init_config_dir()
  OBP_API_HOST = click.prompt("Please enter your API_HOST: ", 
                              default=get_config("OBP_API_HOST",
                              default="http://127.0.0.1:8080",
                              allow_stdin=False))
  set_obp_api_host(OBP_API_HOST)
  OBP_USERNAME = click.prompt("Please enter your username: ",
                              default=get_config("OBP_USERNAME",
                              allow_stdin=False))
  set_obp_username(OBP_USERNAME)
  OBP_PASSWORD = click.prompt("Please enter your password: ", hide_input=True,
                              confirmation_prompt=True)
  set_obp_password(OBP_PASSWORD)
  
  click.echo("... generating direct login token")
  if get_config("OBP_CONSUMER_KEY", allow_stdin=False) is False:
    click.echo("Consumer key needed to generate a DirectLogin token")
    click.confirm("Do you have a consumer key?")
    if click.confirm("Would you like to generate one?", abort=True):
      exit("Not implemented. Visit {}, login, click \"Get an api key\" "
           "and register a consumer. This will give you a consumer key"
           " which you can use here.".format(OBP_API_HOST))
  else:
    OBP_CONSUMER_KEY = click.prompt("Please enter your OBP_CONSUMER_KEY: ",
                                    default=get_config("OBP_CONSUMER_KEY",
                                    allow_stdin=False))
    set_obp_consumer_key(OBP_CONSUMER_KEY)
    
  req = getAuthToken()
  if req.status_code == 201 or req.status_code == 200:
    authToken = json.loads(req.text)['token']
    set_obp_auth_token(authToken)
    # Get & set user id
    req = getUserId()
    if req.status_code == 201 or req.status_code == 200:
      set_obp_user_id(json.loads(req.text)['user_id']) 
    else:
      click.echo("Unable to get your user_id")
      exit(req.text)
  else:
    exit(req.text)

  click.echo("Init complete")

@cli.command(help="🔑 Get your DirectLogin token")
def getauth():
  authToken = getAuthToken()
  print(json.loads(authToken.text))

@cli.command(help="😃 Get your user info")
def getuser():
  req = getUserId()
  if req.status_code == 201 or req.status_code == 200:
    click.echo(req.text)
  else:
    exit(req.text)

@cli.command(help="📋 Get your user id")
def getuserid():
  req = getUserId()
  if req.status_code == 201 or req.status_code == 200:
    user_id = json.loads(req.text)['user_id']
    click.echo({'user_id': user_id})
  else:
    exit(req.text)

@cli.command(help="📋 Get user id by username")
@click.option('--username', prompt=True)
def getuseridbyusername(username):
  req = getUserIdByUsername(username=username)
  if req.status_code == 201 or req.status_code == 200:
    user_id = json.loads(req.text)['user_id']
    click.echo({'user_id': user_id})
  else:
    exit(req.text)

@cli.command(help="🏦 Get list of banks")
def getbanks():
  req = getBanks()
  if req.status_code == 200:
    pp = pprint.PrettyPrinter(width=41, compact=True)
    click.echo(pp.pprint(json.loads(req.text)))
  else:
    exit(req.text)

@cli.command(help="📁 Get list of accounts held")
@click.option('--bank-id', prompt=True)
def getaccountsheld(bank_id):
  req = getAccountsHeld(bank_id)
  if req.status_code == 200:
    pp = pprint.PrettyPrinter(width=41, compact=True)
    click.echo(pp.pprint(json.loads(req.text)))
  else:
    exit(req.text)

@cli.command(help="📁 Get account by id (includes balance)")
@click.option('--bank-id', prompt=True)
@click.option('--account-id', prompt=True)
def getaccountbyid(bank_id, account_id):
  req = getAccountById(bank_id=bank_id, account_id=account_id)
  if req.status_code == 200:
    pp = pprint.PrettyPrinter(width=41, compact=True)
    click.echo(pp.pprint(json.loads(req.text)))
  else:
    exit(req.text)

@cli.command(help="📝 Add a user")
@click.option('--username', prompt=True)
@click.option('--email', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
@click.option('--firstname', prompt=True)
@click.option('--lastname', prompt=True)
def adduser(username, email, password, firstname, lastname):
  req = addUser(username=username, email=email, password=password, 
                firstname=firstname, lastname=lastname)
  if req.status_code == 201 or req.status_code == 200:
    click.echo(req.text)
  else:
    exit(req.text)

@cli.command(help="📁 Add a bank account")
@click.option('--userid', prompt=True, help="Use 'obp getuserid' to find it")
@click.option('--accountid', default="abc123", prompt=True, help="Your choice of account id")
@click.option('--label', default="Label", prompt=True)
@click.option('--type', default="CURRENT", prompt=True)
@click.option('--currency', default="EUR", prompt=True)
@click.option('--branchid', default="1234", prompt=True)
@click.option('--bankid', prompt=True, help="Try getbanks")
def addaccount(userid, accountid, label, type, currency, branchid, bankid):

  req = createAccount(userid=userid, label=label, type=type,
                      currency=currency, bankid=bankid, 
                      branchid=branchid, accountid=accountid)
  if req.status_code == 201 or req.status_code == 200:
    click.echo(req.text)
  else:
    exit(req.text)

@cli.command(help="🚧 Add a role for current user")
@click.option('--role-name', required=True, help="Name of the role/entitelment")
@click.option('--bank-id', required=False, help="Some roles need a bank id")
@click.option('--user-id', required=False, help="Add role to a differnt user")
def addrole(role_name, bank_id=None, user_id=None):
  if bank_id is None:
    req = addRole(role=role_name, user_id=user_id)
  else:
    req = addRole(role=role_name, bank_id=bank_id, user_id=user_id)
  if req.status_code == 201 or req.status_code == 200:
    click.echo(req.text)
  else:
    exit(req.text)

@cli.command(help="📉 Add exchange rate (FX)")
@click.option('--bank-id', required=True, prompt=True)
@click.option('--from-currency', required=True, prompt=True)
@click.option('--to-currency', required=True, prompt=True)
@click.option('--conversion-value', required=True, prompt=True)
@click.option('--inverse-conversion-value', required=True, prompt=True)
@click.option('--effective-date', required=True, prompt=True, 
              help="2017-09-19T00:00:00Z")
def addfx(bank_id, from_currency, to_currency, conversion_value,
          inverse_conversion_value, effective_date):
  req = addFx(bank_id, from_currency, to_currency, conversion_value,
              inverse_conversion_value, effective_date)
  if req.status_code == 201 or req.status_code == 200:
    click.echo(req.text)
  else:
    exit(req.text)

@cli.command(help="⚠️  🏦 Delete all branches")
@click.option('--bank-id', required=True)
def deletebranches(bank_id):
  req = deleteBranches(bank_id)

@cli.command(help="🚜 Import branches from spreadsheet template")
@click.argument('spreadsheet', type=click.File('rb'), required=True)
def importbranches(spreadsheet):
  req = importBranches(spreadsheet)

@cli.command(help="🚜 Import accounts from spreadsheet template")
@click.argument('spreadsheet', type=click.File('rb'), required=True)
def importaccounts(spreadsheet):
  req = importAccounts(spreadsheet)

@cli.command(help="🚜 Import users from spreadsheet template")
@click.argument('spreadsheet', type=click.File('rb'), required=True)
def importusers(spreadsheet):
  req = importUsers(spreadsheet)

@cli.command(help="🚜 Import transactions from spreadsheet template")
@click.argument('spreadsheet', type=click.File('rb'), required=True)
def importtransactions(spreadsheet):
  req = importTransactions(spreadsheet)

@cli.command(help="🚜 Import customers from spreadsheet template")
@click.argument('spreadsheet', type=click.File('rb'), required=True)
def importcustomers(spreadsheet):
  req = importCustomers(spreadsheet)
