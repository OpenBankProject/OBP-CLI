import click
from .auth_direct_login import getAuthToken

@click.group()
def cli():
  pass


@cli.command()
def init():
  OBP_API_HOST = click.prompt("Please enter your API_HOST: ", 
                              default="http://127.0.0.1:8080")
  OBP_USERNAME = click.prompt("Please enter your username: ")
  OBP_PASSWORD = click.prompt("Please enter your password: ", hide_input=True, confirmation_prompt=True)
  click.echo("... generating direct login token")
  click.echo("... storing direct login token in user config path")
  click.echo("Init complete")

@cli.command()
def getauth():
  authToken = getAuthToken()
  print(authToken)
