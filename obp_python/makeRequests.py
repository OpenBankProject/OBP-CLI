import requests
from .init import get_config

authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
headers = {'Content-Type': 'application/json',
           'Authorization': authorization}


def check403status(req):
    if req.status_code == 403:
        print(req.text)
        exit(-1)

    return req


def makeGetRequest(url):
    req = requests.get(url, headers=headers)
    return check403status(req)


def makePutRequest(url,payload):
    req = requests.put(url, headers=headers, json=payload)
    return check403status(req)


def makePostRequest(url,payload):
    req = requests.post(url, headers=headers, json=payload)
    return check403status(req)
