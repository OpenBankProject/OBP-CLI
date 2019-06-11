from appdirs import AppDirs
import os
from pathlib import Path

appname = "obp"
appauthor = "Open Bank Project"
appDirs = AppDirs(appname, appauthor)
confDir = appDirs.user_config_dir

def init_config_dir():
  os.makedirs(confDir, exist_ok=True)

def write_config(NAME, VALUE):
  path = os.path.join(confDir, NAME)

  if os.path.isfile(path) is False:
    init_config_dir()

  with open(os.path.join(confDir, NAME), 'w') as fp:
    fp.write(str(VALUE))

def get_config(NAME, default=None, allow_stdin=True):
  path = os.path.join(confDir, NAME)
  if os.path.isfile(path) is False:
    init_config_dir()

  if os.getenv(NAME, False) is not False:
    return os.getenv(NAME)
  else:
    try:  
      with open(os.path.join(confDir, NAME)) as fp:
        return fp.read()
    except FileNotFoundError:
      if allow_stdin:
        return input('{} -->'.format(NAME))
  if default is not None:
    return default
  return None

def set_obp_api_host(OBP_API_HOST):
    write_config("OBP_API_HOST", OBP_API_HOST)

def set_obp_username(OBP_USERNAME):
    write_config("OBP_USERNAME", OBP_USERNAME)

def set_obp_user_id(OBP_USER_ID):
    write_config("OBP_USER_ID", OBP_USER_ID)

def set_obp_password(OBP_PASSWORD):
    write_config("OBP_PASSWORD", OBP_PASSWORD)

def set_obp_auth_token(OBP_AUTH_TOKEN):
    write_config("OBP_AUTH_TOKEN", OBP_AUTH_TOKEN)

def set_obp_consumer_key(OBP_CONSUMER_KEY):
    write_config("OBP_CONSUMER_KEY", OBP_CONSUMER_KEY)

def set_obp_auth_token(OBP_AUTH_TOKEN):
    write_config("OBP_AUTH_TOKEN", OBP_AUTH_TOKEN)
