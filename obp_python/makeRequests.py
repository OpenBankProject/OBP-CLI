import requests
from .init import get_config

def makeGetRequest(url):
    authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
    headers = {'Content-Type': 'application/json',
               'Authorization': authorization}
    req = requests.get(url, headers=headers)

    if req.status_code == 403:
        print(req.text)
        exit(-1)

    return req

def makePutRequest(url,payload):
    authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
    headers = {'Content-Type': 'application/json',
               'Authorization': authorization}
    req = requests.put(url, headers=headers, json=payload)
    if req.status_code == 403:
        print(req.text)
        exit(-1)

    return req

def makePostRequest(url,payload):
    authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
    headers = {'Content-Type': 'application/json',
               'Authorization': authorization}
    req = requests.post(url, headers=headers, json=payload)
    if req.status_code == 403:
        print(req.text)
        exit(-1)

    return req
