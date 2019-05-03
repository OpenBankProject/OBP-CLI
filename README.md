Python Utilities to make working with Open Bank Project api easier

- uses python3

## Install

```
pip install obp-python # Requires at least python 3
```

> If your operating system defaults to python two, you might need to run 
  `pip3 install obp-python # Requires at least python 3` 

## Usage
```
Usage: obp [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  addaccount     📁 Add a bank account
  addrole        🚧 Add a role for current user
  adduser        📝 Add a user
  getauth        🔑 Get your DirectLogin token
  getbanks       🏦 Get list of banks
  getuser        😃 Get your user info
  getuserid      📋 Get your user id
  init           💡 Initalize connection to your Open Bank Project instance
  sandboximport  🚜 Bulk import sandbox data from json input
```


#### Development / Contributing (Development only)

> **Note** You can ignore this is your just using the utlity. This is 
just for developing the utlity.

To work on this utility as a developer:
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

- 0.19 Added sandboximport utility `obp sandboximport --example`
- 0.0.9
Switch to use `OBP_API_HOST` instead of `OBP_ENDPOINT`
