
## Open Bank Project CLI
A command line utility (CLI) to work with the Open Bank Project sandbox called `obp`.

With the obp cli you can:

- Initiate an api connection to the sandbox 
  - *note* you still need to sign-up from the sandbox homepage first to create your username & password
- Get your DirectLogin token
- Get your user information
- Get your user id 
- Get banks 
- Get (your) accounts held at the bank

Also, depending on your account access you may:
- Create a bank account
- Add roles to a user
- Import/Delete branches
- Import dummy bank data 


## Install

- Requires python3
- Requires pip (see https://pip.pypa.io/en/stable/installing/)

```
pip install --user obp-python # Requires at least python 3
```

> Warning: If your operating system defaults to python 2, your pip command might be:

```
pip3 install --user obp-python
#or 
pip3.6 install --user obp-python
```


## Usage
```
Usage: obp [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  addaccount              📁 Add a bank account
  addbank                 🏦 Add a bank
  addcustomer             🧙 Add a customer
  addfx                   📉 Add exchange rate (FX)
  addrole                 🚧 Add a role for current user
  adduser                 📝 Add a user
  answerconsent           🚧 Answer consent
  createconsent           🚧 Add a consent
  deletebranches          ⚠️ 🏦 Delete all branches
  deletecardbyid          ⚠️ 💳 Delete card by id
  getaccountbyid          📁 Get account by id (includes balance)
  getaccountsheld         📁 Get list of accounts held
  getaccounttransactions  📁 Get transactions for an account
  getauth                 🔑 Get your DirectLogin token
  getbanks                🏦 Get list of banks
  getcardbyid             💳 Get card by id
  getcardbynumber         💳 Get card by card number
  getcards                💳 Get list of cards at bank
  getconsents             🚧 Get consents
  getcustomers            👥 Get list of customers
  getuser                 😃 Get your user info
  getuserid               📋 Get your user id
  getuseridbyusername     📋 Get user id by username
  importaccounts          🚜 Import accounts from spreadsheet template
  importbranches          🚜 Import branches from spreadsheet template
  importcardattribues     🚜 Import card attributes from spreadsheet template
  importcards             🚜 Import cards from spreadsheet template
  importcustomers         🚜 Import customers from spreadsheet template
  importtransactions      🚜 Import transactions from spreadsheet template
  importusers             🚜 Import users from spreadsheet template
  init                    💡 Initalize connection to your Open Bank Project...
  linkusertocustomer      🔗 Link user to a customer
  revokeconsent           🚧 Revoke consent
  sandboximport           🚜 Bulk import sandbox data from json input
```

## Examples

You must initalize the obp cli once, by doing:
```
obp init
```

### Generate Direct Login Token
```
obp init 
Please enter your API_HOST: api.example.com
Please enter your username:
Please enter your password: : 
Repeat for confirmation: 
... generating direct login token
Please enter your OBP_CONSUMER_KEY: # Go to api.example.com, then "Get API Key" to generate consumer key.
obp getauth # Displays your DirectLogin token
```


#### Contributing

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
