import click
from .auth_direct_login import getAuthToken

@click.group()
def cli():
  pass

@cli.command()
def getauth():
  authToken = getAuthToken()
  print(authToken)
