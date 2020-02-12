import requests
from .init import get_config

authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
headers = {'Content-Type': 'application/json',
           'Authorization': authorization}


def check4XXstatus(req):
    if req.status_code >= 400:
        print(req.text)
        exit(-1)

    return req


def makeGetRequest(url):
    req = requests.get(url, headers=headers)
    return check4XXstatus(req)


def makePutRequest(url,payload):
    req = requests.put(url, headers=headers, json=payload)
    return check4XXstatus(req)


def makePostRequest(url,payload):
    req = requests.post(url, headers=headers, json=payload)
    return check4XXstatus(req)
