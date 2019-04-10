import click
from .auth_direct_login import getAuthToken

@click.group()
def cli():
  pass


@cli.command()
def init():
  OBP_API_HOST = input("Please enter your API_HOST: ")
  OBP_USERNAME = input("Please enter your username: ")
  print("Init complete")

@cli.command()
def getauth():
  authToken = getAuthToken()
  print(authToken)
