import click
from .auth_direct_login import getAuthToken
from .init import (init_config_dir, set_obp_api_host, set_obp_username, 
                  set_obp_password, set_obp_consumer_key, set_obp_auth_token,
                  get_config)

@click.group()
def cli():
  pass


@cli.command()
def init():
  init_config_dir()
  OBP_API_HOST = click.prompt("Please enter your API_HOST: ", 
                              default="http://127.0.0.1:8080")
  set_obp_api_host(OBP_API_HOST)
  OBP_USERNAME = click.prompt("Please enter your username: ",
                              default=get_config("OBP_USERNAME"))
  set_obp_username(OBP_USERNAME)
  OBP_PASSWORD = click.prompt("Please enter your password: ", hide_input=True,
                              confirmation_prompt=True)
  set_obp_password(OBP_PASSWORD)
  
  click.echo("... generating direct login token")
  if get_config("OBP_CONSUMER_KEY") is False:
    click.echo("Consumer key needed to generate a DirectLogin token")
    click.confirm("Do you have a consumer key?")
    if click.confirm("Would you like to generate one?", abort=True):
      exit("Not implemented. Visit {}, login, click \"Get an api key\" "
           "and register a consumer. This will give you a consumer key"
           " which you can use here.".format(OBP_API_HOST))
  else:
    OBP_CONSUMER_KEY = click.prompt("Please enter your OBP_CONSUMER_KEY: ",
                                    default=get_config("OBP_CONSUMER_KEY"))
    set_obp_consumer_key(OBP_CONSUMER_KEY)
    
  authToken = getAuthToken()
  set_obp_auth_token(authToken)

  click.echo("Init complete")

@cli.command()
def getauth():
  authToken = getAuthToken()
  print(authToken)
