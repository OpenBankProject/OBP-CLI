Python Utilities to make working with Open Bank Project api easier

- uses python3

## Install

```
pip install obp-python # Requires at least python 3
```

## Run a utility

e.g.
```
obp getauth
```

## Utilities

- getauth : Get a direct login token


#### Development / Contributing
**Note** You can ignore this is your just using the utlity. This is 
just for developing the utlity.

To work on this utility as a developer. 
##### Building 

```
# Setup python3 environment
virtualenv -p python3 venv
. venv/bin/activate
git clone <this-repo>
# Building wheels etc
python setup.py sdist bdist_wheel
# Installing your edits locally:
pip install -e <path-to-this-repo> # -e means Install  a  project  in editable mode (i.e.  setuptools "developmode")
# Work on utility..submit pull request 

```
###### Update history

- 0.0.9
Switch to use `OBP_API_HOST` instead of `OBP_ENDPOINT`
