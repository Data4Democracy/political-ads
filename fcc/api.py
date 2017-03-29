import requests
import requests_cache
import simplejson as json
from urllib.request import urlretrieve
import urllib.parse as urlparse
import os

requests_cache.install_cache('fcc', backend='sqlite', allowable_methods=('GET', 'POST'), expire_after=10000000)

baseUrl = "https://publicfiles.fcc.gov/api/"

def callApi(reqUrl, params=None):
    '''
        Holding this here in case we might want to do some rate limits or proxying to local DB
    '''
    if not params: suffix = '.json'
    else: suffix = ''

    response = requests.get(baseUrl + reqUrl + suffix, params=params)
    if response.status_code == 200:
        response = response.json()
        if response['status'] in ['OK', 'success']:
            return response
        else:
            # throw error
            #TODO HANDLE ERRORS
            return None
    else:
        print(response.status_code)

def downloadFile(reqUrl, downloadPath=None):
    if not downloadPath:
        downloadPath = './downloads/'
    file_path = os.path.basename(urlparse.urlparse(reqUrl).path)
    return urlretrieve(baseUrl + reqUrl, downloadPath +file_path)